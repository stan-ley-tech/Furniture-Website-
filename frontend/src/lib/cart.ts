import { writable, derived } from 'svelte/store';
import { browser } from '$app/environment';

export type CartItem = {
	slug: string;
	name: string;
	price: number;
	image: string;
	quantity: number;
};

const STORAGE_KEY = 'ewf-cart';

function loadInitial(): CartItem[] {
	if (!browser) return [];
	try {
		const raw = localStorage.getItem(STORAGE_KEY);
		return raw ? JSON.parse(raw) : [];
	} catch {
		return [];
	}
}

function persist(items: CartItem[]) {
	if (browser) localStorage.setItem(STORAGE_KEY, JSON.stringify(items));
}

function createCart() {
	const { subscribe, update, set } = writable<CartItem[]>(loadInitial());

	return {
		subscribe,
		add(product: Omit<CartItem, 'quantity'>, quantity = 1) {
			update((items) => {
				const existing = items.find((i) => i.slug === product.slug);
				const next = existing
					? items.map((i) =>
							i.slug === product.slug ? { ...i, quantity: i.quantity + quantity } : i
						)
					: [...items, { ...product, quantity }];
				persist(next);
				return next;
			});
		},
		setQuantity(slug: string, quantity: number) {
			update((items) => {
				const next =
					quantity <= 0
						? items.filter((i) => i.slug !== slug)
						: items.map((i) => (i.slug === slug ? { ...i, quantity } : i));
				persist(next);
				return next;
			});
		},
		remove(slug: string) {
			update((items) => {
				const next = items.filter((i) => i.slug !== slug);
				persist(next);
				return next;
			});
		},
		clear() {
			set([]);
			persist([]);
		}
	};
}

export const cart = createCart();

export const cartCount = derived(cart, ($cart) => $cart.reduce((sum, i) => sum + i.quantity, 0));

export const cartTotal = derived(cart, ($cart) =>
	$cart.reduce((sum, i) => sum + i.quantity * i.price, 0)
);

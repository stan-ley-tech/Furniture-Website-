import { env } from '$env/dynamic/public';

const API_BASE = env.PUBLIC_API_BASE_URL ?? 'http://localhost:8001';

export type Product = {
	id: number;
	name: string;
	slug: string;
	category: string;
	price: number;
	description: string;
	image: string;
	in_stock: boolean;
};

export async function getProducts(
	fetchFn: typeof fetch = fetch,
	category?: string
): Promise<Product[]> {
	try {
		const url = category
			? `${API_BASE}/api/products?category=${encodeURIComponent(category)}`
			: `${API_BASE}/api/products`;
		const res = await fetchFn(url);
		if (!res.ok) throw new Error(`API error: ${res.status}`);
		return await res.json();
	} catch (e) {
		console.error('DEBUG getProducts failed. API_BASE=', API_BASE, 'error=', e);
		return [];
	}
}

export async function getProduct(
	slug: string,
	fetchFn: typeof fetch = fetch
): Promise<Product | null> {
	try {
		const res = await fetchFn(`${API_BASE}/api/products/${encodeURIComponent(slug)}`);
		if (!res.ok) return null;
		return await res.json();
	} catch {
		return null;
	}
}

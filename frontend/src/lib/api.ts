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

export async function getProducts(fetchFn: typeof fetch = fetch): Promise<Product[]> {
	try {
		const res = await fetchFn(`${API_BASE}/api/products`);
		if (!res.ok) throw new Error(`API error: ${res.status}`);
		return await res.json();
	} catch {
		return [];
	}
}

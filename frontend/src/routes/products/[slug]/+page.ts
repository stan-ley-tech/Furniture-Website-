import { error } from '@sveltejs/kit';
import { getProduct, getProducts } from '$lib/api';
import { categories } from '$lib/categories';
import type { PageLoad } from './$types';

export const load: PageLoad = async ({ fetch, params }) => {
	const product = await getProduct(params.slug, fetch);
	if (!product) {
		error(404, 'Product not found');
	}

	const categorySlug = categories.find(
		(c) => c.name.toLowerCase() === product.category.toLowerCase()
	)?.slug;

	const related = (await getProducts(fetch, product.category)).filter(
		(p) => p.slug !== product.slug
	);

	return { product, related, categorySlug };
};

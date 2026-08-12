import { error } from '@sveltejs/kit';
import { getProducts } from '$lib/api';
import { getCategory } from '$lib/categories';
import type { PageLoad } from './$types';

export const load: PageLoad = async ({ fetch, params }) => {
	const category = getCategory(params.category);
	if (!category) {
		error(404, 'Category not found');
	}

	const products = await getProducts(fetch, category.name);
	return { category, products };
};

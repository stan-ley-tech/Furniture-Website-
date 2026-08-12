<script lang="ts">
	import ProductCard from '$lib/components/ProductCard.svelte';
	import { categories } from '$lib/categories';
	import type { PageProps } from './$types';

	let { data }: PageProps = $props();
</script>

<svelte:head>
	<title>Shop All &mdash; Elite Wood Furniture</title>
	<meta name="description" content="Browse the full Elite Wood Furniture catalog." />
</svelte:head>

<section class="shop-header container">
	<p class="eyebrow">Shop All</p>
	<h1>The Full Collection</h1>

	<div class="category-links">
		{#each categories as cat}
			<a href="/shop/{cat.slug}">{cat.name}</a>
		{/each}
	</div>
</section>

<section class="container">
	{#if data.products.length > 0}
		<div class="product-grid">
			{#each data.products as product (product.id)}
				<ProductCard {product} showDescription />
			{/each}
		</div>
	{:else}
		<p class="empty">
			Product catalog is unavailable right now &mdash; start the backend API to load live
			inventory.
		</p>
	{/if}
</section>

<style>
	.shop-header {
		padding-top: 3rem;
		padding-bottom: 2.5rem;
	}

	.shop-header h1 {
		font-size: clamp(1.8rem, 3.5vw, 2.5rem);
		margin: 0.5rem 0 1.5rem;
	}

	.category-links {
		display: flex;
		flex-wrap: wrap;
		gap: 0.75rem;
	}

	.category-links a {
		padding: 0.55rem 1.1rem;
		font-size: 0.78rem;
		letter-spacing: 0.06em;
		text-transform: uppercase;
		border: 1px solid var(--color-border);
		color: var(--color-text);
		transition:
			border-color 0.2s ease,
			background 0.2s ease;
	}

	.category-links a:hover {
		border-color: var(--color-accent);
		background: var(--color-bg-alt);
	}

	.product-grid {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 2.5rem 1.5rem;
		padding-bottom: 5rem;
	}

	.empty {
		color: var(--color-text-muted);
		padding: 3rem 0 5rem;
	}

	@media (max-width: 860px) {
		.product-grid {
			grid-template-columns: repeat(2, 1fr);
		}
	}

	@media (max-width: 540px) {
		.product-grid {
			grid-template-columns: 1fr;
		}
	}
</style>

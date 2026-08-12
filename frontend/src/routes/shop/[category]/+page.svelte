<script lang="ts">
	import ProductCard from '$lib/components/ProductCard.svelte';
	import { categories } from '$lib/categories';
	import type { PageProps } from './$types';

	let { data }: PageProps = $props();
</script>

<svelte:head>
	<title>{data.category.name} &mdash; Elite Wood Furniture</title>
	<meta name="description" content={data.category.description} />
</svelte:head>

<section class="shop-header" style="background-image: url('{data.category.image}')">
	<div class="shop-header-content">
		<p class="eyebrow">Shop</p>
		<h1>{data.category.name}</h1>
		<p class="lede">{data.category.description}</p>
	</div>
</section>

<section class="container">
	<div class="category-links">
		<a href="/shop" class:active={false}>All</a>
		{#each categories as cat}
			<a href="/shop/{cat.slug}" class:active={cat.slug === data.category.slug}>{cat.name}</a>
		{/each}
	</div>

	{#if data.products.length > 0}
		<div class="product-grid">
			{#each data.products as product (product.id)}
				<ProductCard {product} showDescription />
			{/each}
		</div>
	{:else}
		<p class="empty">
			No pieces are listed under {data.category.name} yet &mdash; check back soon, or
			<a href="/shop">browse the full collection</a>.
		</p>
	{/if}
</section>

<style>
	.shop-header {
		min-height: 280px;
		display: flex;
		align-items: center;
		background-size: cover;
		background-position: center;
		position: relative;
	}

	.shop-header::before {
		content: '';
		position: absolute;
		inset: 0;
		background: linear-gradient(90deg, rgba(20, 16, 12, 0.72) 0%, rgba(20, 16, 12, 0.2) 70%);
	}

	.shop-header-content {
		position: relative;
		max-width: 32rem;
		padding: 2.5rem var(--gutter);
		color: #f7f5f1;
	}

	.shop-header-content h1 {
		font-size: clamp(1.8rem, 3.5vw, 2.5rem);
		margin: 0.5rem 0 0.75rem;
	}

	.shop-header-content .lede {
		color: #e5ddd0;
		font-size: 1rem;
		line-height: 1.55;
	}

	.category-links {
		display: flex;
		flex-wrap: wrap;
		gap: 0.75rem;
		padding: 2.5rem 0 2rem;
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

	.category-links a:hover,
	.category-links a.active {
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
		padding: 2rem 0 5rem;
	}

	.empty a {
		text-decoration: underline;
		color: var(--color-text);
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

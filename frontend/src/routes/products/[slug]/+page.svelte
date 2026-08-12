<script lang="ts">
	import ProductCard from '$lib/components/ProductCard.svelte';
	import { cart } from '$lib/cart';
	import { cartOpen } from '$lib/ui';
	import type { PageProps } from './$types';

	let { data }: PageProps = $props();

	const priceFormatted = $derived(
		new Intl.NumberFormat('en-KE', {
			style: 'currency',
			currency: 'KES',
			maximumFractionDigits: 0
		}).format(data.product.price)
	);

	function addToCart() {
		cart.add({
			slug: data.product.slug,
			name: data.product.name,
			price: data.product.price,
			image: data.product.image
		});
		cartOpen.set(true);
	}
</script>

<svelte:head>
	<title>{data.product.name} &mdash; Elite Wood Furniture</title>
	<meta name="description" content={data.product.description} />
</svelte:head>

<section class="container breadcrumb">
	<a href="/shop">Shop</a>
	{#if data.categorySlug}
		<span>/</span>
		<a href="/shop/{data.categorySlug}">{data.product.category}</a>
	{/if}
	<span>/</span>
	<span class="current">{data.product.name}</span>
</section>

<section class="container product">
	<div class="product-image">
		<img src={data.product.image} alt={data.product.name} />
	</div>

	<div class="product-info">
		<p class="category">{data.product.category}</p>
		<h1>{data.product.name}</h1>
		<p class="price">{priceFormatted}</p>
		<p class="description">{data.product.description}</p>

		{#if data.product.in_stock}
			<p class="stock in-stock">In Stock</p>
		{:else}
			<p class="stock out-of-stock">Out of Stock</p>
		{/if}

		<button class="btn btn-solid" type="button" onclick={addToCart} disabled={!data.product.in_stock}
			>Add to Cart</button
		>

		<dl class="details">
			<div>
				<dt>Material</dt>
				<dd>Solid hardwood, hand-finished</dd>
			</div>
			<div>
				<dt>Delivery</dt>
				<dd>White-glove delivery, in as little as a week</dd>
			</div>
			<div>
				<dt>Warranty</dt>
				<dd>5-year structural warranty</dd>
			</div>
		</dl>
	</div>
</section>

{#if data.related.length > 0}
	<section class="container related">
		<div class="section-head">
			<h2>You May Also Like</h2>
		</div>
		<div class="product-grid">
			{#each data.related as product (product.id)}
				<ProductCard {product} />
			{/each}
		</div>
	</section>
{/if}

<style>
	.breadcrumb {
		padding-top: 1.5rem;
		font-size: 0.8rem;
		color: var(--color-text-muted);
		display: flex;
		gap: 0.5rem;
	}

	.breadcrumb a {
		color: var(--color-text-muted);
	}

	.breadcrumb a:hover {
		color: var(--color-text);
	}

	.breadcrumb .current {
		color: var(--color-text);
	}

	.product {
		display: grid;
		grid-template-columns: 1.1fr 1fr;
		gap: 3.5rem;
		padding-top: 2rem;
		padding-bottom: 5rem;
	}

	.product-image img {
		width: 100%;
		aspect-ratio: 4 / 5;
		object-fit: cover;
	}

	.product-info {
		padding-top: 0.5rem;
	}

	.category {
		font-size: 0.78rem;
		letter-spacing: 0.1em;
		text-transform: uppercase;
		color: var(--color-text-muted);
		margin-bottom: 0.5rem;
	}

	.product-info h1 {
		font-size: clamp(1.6rem, 3vw, 2.1rem);
		margin-bottom: 0.75rem;
	}

	.price {
		font-size: 1.25rem;
		color: var(--color-accent-dark);
		margin-bottom: 1.25rem;
	}

	.description {
		font-size: 0.95rem;
		line-height: 1.65;
		color: var(--color-text-muted);
		margin-bottom: 1rem;
		max-width: 30rem;
	}

	.stock {
		font-size: 0.8rem;
		letter-spacing: 0.05em;
		text-transform: uppercase;
		margin-bottom: 1.5rem;
	}

	.in-stock {
		color: #3f6b4a;
	}

	.out-of-stock {
		color: #a0453a;
	}

	.details {
		margin-top: 2.5rem;
		border-top: 1px solid var(--color-border);
		padding-top: 1.5rem;
	}

	.details div {
		display: flex;
		justify-content: space-between;
		padding: 0.65rem 0;
		border-bottom: 1px solid var(--color-border);
		font-size: 0.88rem;
	}

	.details dt {
		color: var(--color-text-muted);
	}

	.related {
		padding-bottom: 5rem;
	}

	.section-head {
		margin-bottom: 2rem;
	}

	.section-head h2 {
		font-size: 1.4rem;
	}

	.product-grid {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 2.5rem 1.5rem;
	}

	@media (max-width: 860px) {
		.product {
			grid-template-columns: 1fr;
			gap: 2rem;
		}

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

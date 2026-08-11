<script lang="ts">
	import type { Product } from '$lib/api';

	let { product }: { product: Product } = $props();

	const priceFormatted = $derived(
		new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(product.price)
	);
</script>

<a class="card" href="/">
	<div class="thumb">
		<img src={product.image} alt={product.name} loading="lazy" />
	</div>
	<p class="category">{product.category}</p>
	<h3>{product.name}</h3>
	<p class="price">{priceFormatted}</p>
</a>

<style>
	.card {
		display: block;
	}

	.thumb {
		aspect-ratio: 4 / 5;
		overflow: hidden;
		background: var(--color-bg-alt);
		margin-bottom: 1rem;
	}

	.thumb img {
		width: 100%;
		height: 100%;
		object-fit: cover;
		transition:
			transform 0.35s ease,
			opacity 0.2s ease;
	}

	.card:hover .thumb img {
		transform: scale(1.04);
		opacity: 0.92;
	}

	.category {
		font-size: 0.72rem;
		letter-spacing: 0.1em;
		text-transform: uppercase;
		color: var(--color-text-muted);
		margin-bottom: 0.3rem;
	}

	h3 {
		font-size: 1rem;
		font-weight: 500;
		margin-bottom: 0.35rem;
	}

	.price {
		font-size: 0.92rem;
		color: var(--color-text-muted);
	}
</style>

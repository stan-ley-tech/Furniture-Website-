<script lang="ts">
	import type { Product } from '$lib/api';

	let { product }: { product: Product } = $props();

	const priceFormatted = $derived(
		new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(product.price)
	);
</script>

<a class="card" href="/">
	<div class="thumb" style="--tone: {(product.id * 47) % 360}deg">
		<span>{product.name}</span>
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
		background: linear-gradient(
			160deg,
			hsl(var(--tone) 18% 88%) 0%,
			hsl(var(--tone) 22% 74%) 100%
		);
		display: flex;
		align-items: center;
		justify-content: center;
		text-align: center;
		padding: 1.5rem;
		margin-bottom: 1rem;
		transition: opacity 0.2s ease;
	}

	.card:hover .thumb {
		opacity: 0.85;
	}

	.thumb span {
		font-family: var(--font-display);
		font-size: 0.85rem;
		letter-spacing: 0.04em;
		color: rgba(32, 29, 26, 0.55);
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

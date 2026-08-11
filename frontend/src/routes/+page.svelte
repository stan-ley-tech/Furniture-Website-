<script lang="ts">
	import ProductCard from '$lib/components/ProductCard.svelte';
	import type { PageProps } from './$types';

	let { data }: PageProps = $props();

	const categories = [
		{ name: 'Living Room', hue: '28deg' },
		{ name: 'Dining Room', hue: '150deg' },
		{ name: 'Bedroom', hue: '210deg' },
		{ name: 'Outdoor', hue: '95deg' }
	];
</script>

<svelte:head>
	<title>Elite Wood Furniture — Solid Wood, Handcrafted for Life</title>
	<meta
		name="description"
		content="Elite Wood Furniture crafts solid-wood living, dining, and bedroom furniture built to last generations."
	/>
</svelte:head>

<section class="hero">
	<div class="hero-copy">
		<p class="eyebrow">The 2026 Collection</p>
		<h1>Furniture built from real wood, made to outlast trends.</h1>
		<p class="lede">
			Every piece is hand-finished from sustainably sourced hardwood — designed for everyday life
			and built to be handed down.
		</p>
		<a class="btn btn-solid" href="/">Shop the Collection</a>
	</div>
</section>

<section class="categories container">
	<div class="section-head">
		<h2>Shop by Room</h2>
	</div>
	<div class="category-grid">
		{#each categories as cat}
			<a class="category-tile" href="/" style="--tone: {cat.hue}">
				<span>{cat.name}</span>
			</a>
		{/each}
	</div>
</section>

<section class="featured container">
	<div class="section-head">
		<h2>Best Sellers</h2>
		<a class="btn" href="/">View All</a>
	</div>

	{#if data.products.length > 0}
		<div class="product-grid">
			{#each data.products as product (product.id)}
				<ProductCard {product} />
			{/each}
		</div>
	{:else}
		<p class="empty">
			Product catalog is unavailable right now &mdash; start the backend API to load live
			inventory.
		</p>
	{/if}
</section>

<section class="story">
	<div class="container story-inner">
		<p class="eyebrow">Our Craft</p>
		<h2>Solid wood. Honest joinery. No shortcuts.</h2>
		<p class="lede">
			Elite Wood Furniture partners with independent woodworkers to build furniture the way it
			used to be made — mortise-and-tenon joints, kiln-dried hardwood, and finishes that age
			beautifully.
		</p>
		<a class="btn" href="/">Read Our Story</a>
	</div>
</section>

<style>
	.hero {
		height: min(78vh, 720px);
		display: flex;
		align-items: flex-end;
		background: linear-gradient(180deg, var(--color-bg-alt) 0%, #d9cfc0 100%);
		padding: 0 var(--gutter) 4rem;
	}

	.hero-copy {
		max-width: 34rem;
	}

	.hero-copy h1 {
		font-size: clamp(2.2rem, 4.5vw, 3.4rem);
		line-height: 1.1;
		margin: 0.75rem 0 1.25rem;
	}

	.lede {
		color: var(--color-text-muted);
		font-size: 1.05rem;
		line-height: 1.6;
		margin-bottom: 1.75rem;
	}

	.section-head {
		display: flex;
		align-items: baseline;
		justify-content: space-between;
		margin: 4rem 0 2rem;
	}

	.section-head h2 {
		font-size: 1.6rem;
	}

	.category-grid {
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		gap: 1.25rem;
	}

	.category-tile {
		aspect-ratio: 3 / 4;
		display: flex;
		align-items: flex-end;
		padding: 1.25rem;
		background: linear-gradient(160deg, hsl(var(--tone) 20% 85%) 0%, hsl(var(--tone) 24% 68%) 100%);
	}

	.category-tile span {
		font-family: var(--font-display);
		font-size: 1rem;
		letter-spacing: 0.03em;
		color: #201d1a;
		background: rgba(247, 245, 241, 0.85);
		padding: 0.4rem 0.8rem;
	}

	.product-grid {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 2.5rem 1.5rem;
	}

	.empty {
		color: var(--color-text-muted);
		padding: 3rem 0;
	}

	.story {
		background: var(--color-bg-alt);
		margin-top: 5rem;
		padding: 5rem 0;
	}

	.story-inner {
		max-width: 40rem;
	}

	.story h2 {
		font-size: 2rem;
		margin: 0.75rem 0 1.25rem;
	}

	@media (max-width: 860px) {
		.category-grid {
			grid-template-columns: repeat(2, 1fr);
		}

		.product-grid {
			grid-template-columns: repeat(2, 1fr);
		}

		.hero {
			height: auto;
			padding-top: 4rem;
		}
	}

	@media (max-width: 540px) {
		.product-grid {
			grid-template-columns: 1fr;
		}
	}
</style>

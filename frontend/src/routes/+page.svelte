<script lang="ts">
	import ProductCard from '$lib/components/ProductCard.svelte';
	import type { PageProps } from './$types';

	let { data }: PageProps = $props();

	const categories = [
		{ name: 'Living Room', image: '/images/categories/living-room.jpg' },
		{ name: 'Dining Room', image: '/images/categories/dining-room.jpg' },
		{ name: 'Bedroom', image: '/images/categories/bedroom.jpg' },
		{ name: 'Outdoor', image: '/images/categories/outdoor.jpg' }
	];
</script>

<svelte:head>
	<title>Elite Wood Furniture — Solid Wood, Handcrafted for Life</title>
	<meta
		name="description"
		content="Elite Wood Furniture crafts solid-wood living, dining, and bedroom furniture built to last generations."
	/>
</svelte:head>

<section class="hero" style="background-image: url('/images/hero/living-room-hero.jpg')">
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
			<a class="category-tile" href="/">
				<img src={cat.image} alt={cat.name} loading="lazy" />
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
		background-size: cover;
		background-position: center;
		position: relative;
		padding: 0 var(--gutter) 4rem;
	}

	.hero::before {
		content: '';
		position: absolute;
		inset: 0;
		background: linear-gradient(180deg, rgba(32, 29, 26, 0) 40%, rgba(32, 29, 26, 0.55) 100%);
	}

	.hero-copy {
		position: relative;
		max-width: 34rem;
		color: #f7f5f1;
	}

	.hero-copy .eyebrow {
		color: #e5ddd0;
	}

	.hero-copy .lede {
		color: #ded5c6;
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
		position: relative;
		aspect-ratio: 3 / 4;
		display: flex;
		align-items: flex-end;
		padding: 1.25rem;
		overflow: hidden;
	}

	.category-tile img {
		position: absolute;
		inset: 0;
		width: 100%;
		height: 100%;
		object-fit: cover;
		transition: transform 0.35s ease;
	}

	.category-tile:hover img {
		transform: scale(1.04);
	}

	.category-tile span {
		position: relative;
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

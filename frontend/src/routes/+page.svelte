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
	<div class="hero-caption">
		<p class="hero-caption-eyebrow">In the Collection<br />Quiet Corners</p>
		<p class="hero-caption-body">
			Solid oak seating and warm textiles, styled the way our pieces live in a real home.
		</p>
	</div>

	<div class="hero-overlay">
		<h1>Made to Keep</h1>
		<p class="lede">
			Solid hardwood furniture, hand-finished in small batches for lasting quality.
		</p>
		<div class="hero-actions">
			<a class="btn-ghost" href="/">Shop Living Room</a>
			<a class="btn-ghost" href="/">Shop All New</a>
		</div>
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
		height: min(82vh, 760px);
		position: relative;
		background-size: cover;
		background-position: 62% 32%;
	}

	.hero::before {
		content: '';
		position: absolute;
		inset: 0;
		background: linear-gradient(
			180deg,
			rgba(20, 16, 12, 0.28) 0%,
			rgba(20, 16, 12, 0.22) 45%,
			rgba(20, 16, 12, 0.78) 100%
		);
	}

	.hero-caption {
		position: absolute;
		left: var(--gutter);
		top: 34%;
		max-width: 19rem;
		padding-left: 1.1rem;
		border-left: 1px solid rgba(247, 245, 241, 0.75);
		color: #f7f5f1;
		text-shadow: 0 1px 8px rgba(15, 12, 9, 0.7);
	}

	.hero-caption-eyebrow {
		font-family: var(--font-display);
		font-size: 0.78rem;
		font-weight: 500;
		letter-spacing: 0.08em;
		text-transform: uppercase;
		line-height: 1.5;
	}

	.hero-caption-body {
		margin-top: 0.6rem;
		font-size: 0.85rem;
		line-height: 1.55;
		color: #e5ddd0;
	}

	.hero-overlay {
		position: absolute;
		left: 50%;
		bottom: 3rem;
		transform: translateX(-50%);
		text-align: center;
		color: #f7f5f1;
		width: min(34rem, calc(100% - 2 * var(--gutter)));
	}

	.hero-overlay h1 {
		font-size: clamp(1.8rem, 3.4vw, 2.6rem);
		font-weight: 400;
		letter-spacing: 0.02em;
	}

	.hero-overlay .lede {
		margin: 0.6rem 0 1.5rem;
		color: #ded5c6;
		font-size: 0.95rem;
	}

	.hero-actions {
		display: flex;
		justify-content: center;
		gap: 0.75rem;
		flex-wrap: wrap;
	}

	.btn-ghost {
		padding: 0.85rem 1.5rem;
		font-size: 0.75rem;
		letter-spacing: 0.12em;
		text-transform: uppercase;
		color: #f7f5f1;
		background: rgba(32, 29, 26, 0.3);
		border: 1px solid rgba(247, 245, 241, 0.6);
		backdrop-filter: blur(2px);
		transition:
			background 0.2s ease,
			border-color 0.2s ease;
	}

	.btn-ghost:hover {
		background: rgba(32, 29, 26, 0.55);
		border-color: #f7f5f1;
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
			height: 640px;
		}
	}

	@media (max-width: 640px) {
		.hero-caption {
			display: none;
		}
	}

	@media (max-width: 540px) {
		.product-grid {
			grid-template-columns: 1fr;
		}
	}
</style>

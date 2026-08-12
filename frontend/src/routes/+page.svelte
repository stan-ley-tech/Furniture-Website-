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

<section class="hero" style="background-image: url('/images/sections/our-craft.jpg')">
	<video class="hero-video" autoplay muted loop playsinline poster="/images/sections/our-craft.jpg">
		<source src="/videos/craft-hero.mp4" type="video/mp4" />
	</video>

	<div class="hero-caption">
		<p class="hero-caption-eyebrow">Behind the Scenes<br />In the Workshop</p>
		<p class="hero-caption-body">
			Every piece starts as rough-sawn hardwood, shaped and joined entirely by hand.
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

<section
	class="design-cta"
	style="background-image: url('/images/sections/design-consultation.jpg')"
>
	<div class="design-cta-content">
		<h2>Get a Free Design Consultation</h2>
		<p>Tell us about your space and one of our designers will help you plan it.</p>
		<a class="btn btn-solid-light" href="/">Get Started</a>
	</div>
</section>

<section class="story">
	<div class="container story-grid">
		<div>
			<p class="eyebrow">Our Craft</p>
			<h2>Solid wood. Honest joinery. No shortcuts.</h2>
			<p class="lede">
				Elite Wood Furniture partners with independent woodworkers to build furniture the way it
				used to be made — mortise-and-tenon joints, kiln-dried hardwood, and finishes that age
				beautifully.
			</p>
			<a class="btn" href="/">Read Our Story</a>
		</div>
		<div class="story-image">
			<img src="/images/sections/our-craft.jpg" alt="Craftsman hand-cutting a wood joint" loading="lazy" />
		</div>
	</div>
</section>

<style>
	.hero {
		height: min(82vh, 760px);
		position: relative;
		background-size: cover;
		background-position: center;
		overflow: hidden;
	}

	.hero-video {
		position: absolute;
		inset: 0;
		z-index: 0;
		width: 100%;
		height: 100%;
		object-fit: cover;
	}

	@media (prefers-reduced-motion: reduce) {
		.hero-video {
			display: none;
		}
	}

	.hero::before {
		content: '';
		position: absolute;
		inset: 0;
		z-index: 1;
		background: linear-gradient(
			180deg,
			rgba(20, 16, 12, 0.32) 0%,
			rgba(20, 16, 12, 0.26) 45%,
			rgba(20, 16, 12, 0.8) 100%
		);
	}

	.hero-caption {
		position: absolute;
		z-index: 2;
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
		z-index: 2;
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

	.design-cta {
		margin-top: 5rem;
		min-height: 320px;
		display: flex;
		align-items: center;
		background-size: cover;
		background-position: center;
		position: relative;
	}

	.design-cta::before {
		content: '';
		position: absolute;
		inset: 0;
		background: linear-gradient(90deg, rgba(20, 16, 12, 0.72) 0%, rgba(20, 16, 12, 0.18) 65%);
	}

	.design-cta-content {
		position: relative;
		max-width: 26rem;
		padding: 3rem var(--gutter);
		color: #f7f5f1;
	}

	.design-cta-content h2 {
		font-size: clamp(1.5rem, 2.6vw, 2rem);
		font-weight: 400;
	}

	.design-cta-content p {
		margin: 0.75rem 0 1.5rem;
		color: #e5ddd0;
		font-size: 0.95rem;
		line-height: 1.55;
	}

	.btn-solid-light {
		display: inline-flex;
		align-items: center;
		justify-content: center;
		padding: 0.85rem 2rem;
		font-size: 0.8rem;
		letter-spacing: 0.14em;
		text-transform: uppercase;
		background: #f7f5f1;
		color: #201d1a;
		border: 1px solid #f7f5f1;
		border-radius: 999px;
		transition: background 0.2s ease;
	}

	.btn-solid-light:hover {
		background: transparent;
		color: #f7f5f1;
	}

	.story {
		background: var(--color-bg-alt);
		margin-top: 5rem;
		padding: 5rem 0;
	}

	.story-grid {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 3rem;
		align-items: center;
	}

	.story h2 {
		font-size: 2rem;
		margin: 0.75rem 0 1.25rem;
	}

	.story-image img {
		width: 100%;
		aspect-ratio: 4 / 3;
		object-fit: cover;
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

		.story-grid {
			grid-template-columns: 1fr;
		}

		.story-image {
			order: -1;
		}

		.design-cta::before {
			background: linear-gradient(180deg, rgba(20, 16, 12, 0.35) 0%, rgba(20, 16, 12, 0.75) 100%);
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

<svelte:head>
	<title>Our Story &mdash; Elite Wood Furniture</title>
	<meta
		name="description"
		content="Elite Wood Furniture partners with independent woodworkers to build solid-wood furniture the way it used to be made."
	/>
</svelte:head>

<section class="hero-block" style="background-image: url('/images/sections/our-craft.jpg')">
	<div class="hero-block-content">
		<p class="eyebrow">Our Story</p>
		<h1>Furniture Built to Outlast Trends</h1>
	</div>
</section>

<section class="container story-body">
	<p class="lede">
		Elite Wood Furniture started with a simple frustration: most furniture on the market today is
		built to be replaced, not kept. Particleboard cores, stapled joints, finishes that wear
		through in a year. We wanted something different.
	</p>
	<p>
		We partner with a small network of independent woodworkers who build the way furniture used to
		be built &mdash; solid hardwood, mortise-and-tenon joinery, finishes that are meant to age
		rather than fail. Every piece in our collection is made in small batches, not mass-produced,
		which means more attention per piece and a supply chain we can actually stand behind.
	</p>
	<p>
		It also means our furniture costs more than particleboard alternatives &mdash; and lasts
		decades longer. We think that's a trade worth making, and we built this company for customers
		who agree.
	</p>

	<div class="values">
		<div>
			<h3>Solid Hardwood</h3>
			<p>No particleboard, no veneer over MDF. If it looks like wood, it is wood.</p>
		</div>
		<div>
			<h3>Small-Batch Craft</h3>
			<p>Built by independent woodworkers in small runs, not mass-produced on an assembly line.</p>
		</div>
		<div>
			<h3>Built to Repair</h3>
			<p>Joinery and finishes chosen so pieces can be repaired and refinished, not replaced.</p>
		</div>
	</div>

	<a class="btn btn-solid" href="/shop">Shop the Collection</a>
</section>

<style>
	.hero-block {
		height: 320px;
		display: flex;
		align-items: center;
		background-size: cover;
		background-position: center;
		position: relative;
	}

	.hero-block::before {
		content: '';
		position: absolute;
		inset: 0;
		background: rgba(20, 16, 12, 0.5);
	}

	.hero-block-content {
		position: relative;
		max-width: 40rem;
		padding: 0 var(--gutter);
		color: #f7f5f1;
		text-align: center;
		margin: 0 auto;
	}

	.hero-block-content h1 {
		font-size: clamp(1.8rem, 4vw, 2.6rem);
		margin-top: 0.5rem;
	}

	.story-body {
		max-width: 42rem;
		padding: 4rem var(--gutter) 6rem;
	}

	.story-body .lede {
		font-size: 1.1rem;
		line-height: 1.6;
		margin-bottom: 1.5rem;
	}

	.story-body p {
		color: var(--color-text-muted);
		line-height: 1.7;
		margin-bottom: 1.25rem;
	}

	.values {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 2rem;
		margin: 3rem 0;
		padding: 2.5rem 0;
		border-top: 1px solid var(--color-border);
		border-bottom: 1px solid var(--color-border);
	}

	.values h3 {
		font-family: var(--font-mono);
		font-size: 0.78rem;
		font-weight: 700;
		letter-spacing: 0.04em;
		text-transform: uppercase;
		color: var(--color-text);
		margin-bottom: 0.6rem;
	}

	.values p {
		font-size: 0.88rem;
		margin-bottom: 0;
	}

	@media (max-width: 640px) {
		.values {
			grid-template-columns: 1fr;
			gap: 1.75rem;
		}
	}
</style>

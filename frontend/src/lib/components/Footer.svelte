<script lang="ts">
	import { categories } from '$lib/categories';
</script>

<footer>
	<div class="container grid">
		<div class="brand">
			<h3>Elite Wood <span>Furniture</span></h3>
			<p>Handcrafted furniture in solid wood, built to last generations.</p>
		</div>

		<div>
			<p class="eyebrow">Shop</p>
			{#each categories as cat}
				<a href="/shop/{cat.slug}">{cat.name}</a>
			{/each}
		</div>

		<div>
			<p class="eyebrow">Company</p>
			<a href="/our-story">Our Story</a>
			<a href="/sustainability">Sustainability</a>
			<a href="/our-story">Craftsmanship</a>
			<a href="/careers">Careers</a>
		</div>

		<div>
			<p class="eyebrow">Support</p>
			<a href="/contact">Contact Us</a>
			<a href="/shipping-returns">Shipping &amp; Returns</a>
			<a href="/warranty">Warranty</a>
			<a href="/faq">FAQ</a>
		</div>

		<div class="newsletter">
			<p class="eyebrow">Stay in Touch</p>
			<p>Sign up for design tips and new collection previews.</p>
			<form onsubmit={(e) => e.preventDefault()}>
				<input type="email" placeholder="Email address" required />
				<button class="btn btn-solid" type="submit">Join</button>
			</form>
		</div>
	</div>

	<div class="container bottom">
		<p>&copy; {new Date().getFullYear()} Elite Wood Furniture. All rights reserved.</p>
	</div>
</footer>

<style>
	footer {
		background: var(--color-bg-alt);
		border-top: 1px solid var(--color-border);
		margin-top: 5rem;
		padding-top: 4rem;
	}

	.grid {
		display: grid;
		grid-template-columns: 1.6fr 1fr 1fr 1fr 1.6fr;
		gap: 2rem;
		padding-bottom: 3rem;
	}

	.brand h3 {
		font-size: 1.2rem;
		margin-bottom: 0.75rem;
	}

	.brand span {
		font-weight: 300;
		color: var(--color-accent);
	}

	.brand p,
	.newsletter p:not(.eyebrow) {
		color: var(--color-text-muted);
		font-size: 0.9rem;
		line-height: 1.6;
	}

	.eyebrow {
		margin-bottom: 0.9rem;
	}

	div > a {
		display: block;
		font-size: 0.9rem;
		color: var(--color-text-muted);
		padding: 0.3rem 0;
	}

	div > a:hover {
		color: var(--color-text);
	}

	.newsletter form {
		display: flex;
		margin-top: 1rem;
		gap: 0.5rem;
	}

	.newsletter input {
		flex: 1;
		min-width: 0;
		padding: 0.7rem 0.9rem;
		border: 1px solid var(--color-border);
		background: var(--color-surface);
		font-size: 0.85rem;
	}

	.bottom {
		border-top: 1px solid var(--color-border);
		padding: 1.5rem var(--gutter);
	}

	.bottom p {
		font-size: 0.78rem;
		color: var(--color-text-muted);
	}

	@media (max-width: 860px) {
		.grid {
			grid-template-columns: 1fr 1fr;
		}

		.brand,
		.newsletter {
			grid-column: 1 / -1;
		}
	}
</style>

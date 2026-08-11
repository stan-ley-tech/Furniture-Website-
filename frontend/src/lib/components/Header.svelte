<script lang="ts">
	const links = ['New Arrivals', 'Living', 'Dining', 'Bedroom', 'Storage', 'Outdoor', 'Sale'];
	let menuOpen = $state(false);
</script>

<div class="announcement">Free shipping on orders over $99 &mdash; Handcrafted, sustainably sourced wood furniture</div>

<header>
	<div class="container bar">
		<button class="menu-toggle" onclick={() => (menuOpen = !menuOpen)} aria-label="Toggle menu">
			☰
		</button>

		<a href="/" class="logo">Elite Wood <span>Furniture</span></a>

		<nav class:open={menuOpen}>
			{#each links as link}
				<a href="/">{link}</a>
			{/each}
		</nav>

		<div class="actions">
			<button aria-label="Search">Search</button>
			<button aria-label="Account">Account</button>
			<button aria-label="Cart">Cart (0)</button>
		</div>
	</div>
</header>

<style>
	.announcement {
		background: var(--color-text);
		color: var(--color-bg);
		text-align: center;
		font-size: 0.75rem;
		letter-spacing: 0.06em;
		padding: 0.6rem 1rem;
	}

	header {
		background: var(--color-surface);
		border-bottom: 1px solid var(--color-border);
		position: sticky;
		top: 0;
		z-index: 20;
	}

	.bar {
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 1.5rem;
		padding-top: 1.1rem;
		padding-bottom: 1.1rem;
	}

	.logo {
		font-family: var(--font-display);
		font-size: 1.35rem;
		letter-spacing: 0.04em;
		white-space: nowrap;
	}

	.logo span {
		font-weight: 300;
		color: var(--color-accent);
	}

	nav {
		display: flex;
		gap: 1.75rem;
		flex: 1;
		justify-content: center;
	}

	nav a {
		font-size: 0.78rem;
		letter-spacing: 0.08em;
		text-transform: uppercase;
		color: var(--color-text);
		padding: 0.25rem 0;
		border-bottom: 1px solid transparent;
		transition: border-color 0.2s ease;
	}

	nav a:hover {
		border-color: var(--color-accent);
	}

	.actions {
		display: flex;
		gap: 1.25rem;
	}

	.actions button {
		background: none;
		border: none;
		font-size: 0.75rem;
		letter-spacing: 0.06em;
		text-transform: uppercase;
		color: var(--color-text);
	}

	.menu-toggle {
		display: none;
		background: none;
		border: none;
		font-size: 1.1rem;
		color: var(--color-text);
	}

	@media (max-width: 860px) {
		.menu-toggle {
			display: block;
		}

		nav {
			position: absolute;
			top: 100%;
			left: 0;
			right: 0;
			background: var(--color-surface);
			border-bottom: 1px solid var(--color-border);
			flex-direction: column;
			align-items: flex-start;
			gap: 0;
			padding: 0 var(--gutter);
			max-height: 0;
			overflow: hidden;
			transition: max-height 0.25s ease;
		}

		nav.open {
			max-height: 24rem;
		}

		nav a {
			width: 100%;
			padding: 0.85rem 0;
			border-bottom: 1px solid var(--color-border);
		}

		.actions {
			gap: 0.75rem;
		}

		.actions button:nth-child(1),
		.actions button:nth-child(2) {
			display: none;
		}
	}
</style>

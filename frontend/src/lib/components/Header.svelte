<script lang="ts">
	const links = ['New Arrivals', 'Living', 'Dining', 'Bedroom', 'Storage', 'Outdoor', 'Sale'];
	let menuOpen = $state(false);
</script>

<div class="announcement">
	Free shipping on orders over Ksh 15,000 &mdash; Handcrafted, sustainably sourced wood furniture
</div>

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
			<button class="action" aria-label="Search">
				<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
					<circle cx="11" cy="11" r="7.25" />
					<line x1="21" y1="21" x2="16.2" y2="16.2" stroke-linecap="round" />
				</svg>
				<span>Search</span>
			</button>

			<button class="action" aria-label="Account">
				<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
					<circle cx="12" cy="8.25" r="3.75" />
					<path d="M4.5 20c0-4.14 3.36-7.5 7.5-7.5s7.5 3.36 7.5 7.5" stroke-linecap="round" />
				</svg>
				<span>Account</span>
			</button>

			<button class="action" aria-label="Cart, 0 items">
				<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
					<path
						d="M7 8h10l-.9 10.1a1.5 1.5 0 0 1-1.5 1.4H9.4a1.5 1.5 0 0 1-1.5-1.4L7 8z"
						stroke-linejoin="round"
					/>
					<path d="M9 8V6.5a3 3 0 0 1 6 0V8" stroke-linecap="round" />
				</svg>
				<span>Cart (0)</span>
			</button>
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
		font-family: var(--font-display);
		font-size: 0.8rem;
		font-weight: 500;
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
		gap: 1.75rem;
	}

	.action {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 0.3rem;
		background: none;
		border: none;
		color: var(--color-text);
		opacity: 0.85;
		transition: opacity 0.2s ease;
	}

	.action:hover {
		opacity: 1;
	}

	.action svg {
		width: 21px;
		height: 21px;
	}

	.action span {
		font-family: var(--font-display);
		font-size: 0.68rem;
		font-weight: 500;
		letter-spacing: 0.07em;
		text-transform: uppercase;
		white-space: nowrap;
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
			gap: 1.1rem;
		}

		.action span {
			display: none;
		}

		.action svg {
			width: 22px;
			height: 22px;
		}
	}
</style>

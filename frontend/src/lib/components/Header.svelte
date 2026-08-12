<script lang="ts">
	import Logo from './Logo.svelte';
	import { cartCount } from '$lib/cart';
	import { cartOpen, searchOpen } from '$lib/ui';

	const links = [
		{ label: 'New Arrivals', href: '/shop' },
		{ label: 'Living', href: '/shop/living-room' },
		{ label: 'Dining', href: '/shop/dining-room' },
		{ label: 'Bedroom', href: '/shop/bedroom' },
		{ label: 'Storage', href: '/shop/storage' },
		{ label: 'Outdoor', href: '/shop/outdoor' },
		{ label: 'Sale', href: '/shop' }
	];
	let menuOpen = $state(false);
</script>

<div class="announcement">
	Free shipping on orders over Ksh 15,000 &mdash; Handcrafted, sustainably sourced wood furniture
</div>

<header>
	<div class="container bar">
		<a href="/" class="logo">
			<Logo size={38} />
			<span class="logo-text">Elite Wood <span class="accent">Furniture</span></span>
		</a>

		<nav class:open={menuOpen}>
			{#each links as link}
				<a href={link.href}>{link.label}</a>
			{/each}
		</nav>

		<div class="nav-right">
			<div class="actions">
				<button class="action" aria-label="Search" onclick={() => searchOpen.set(true)}>
					<i class="fa-solid fa-magnifying-glass"></i>
					<span>Search</span>
				</button>

				<a class="action" href="/account" aria-label="Account">
					<i class="fa-solid fa-user"></i>
					<span>Account</span>
				</a>

				<button
					class="action"
					aria-label="Cart, {$cartCount} items"
					onclick={() => cartOpen.set(true)}
				>
					<i class="fa-solid fa-bag-shopping"></i>
					<span>Cart ({$cartCount})</span>
				</button>
			</div>

			<button class="menu-toggle" onclick={() => (menuOpen = !menuOpen)} aria-label="Toggle menu">
				<i class="fa-solid {menuOpen ? 'fa-xmark' : 'fa-bars'}"></i>
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
		display: flex;
		align-items: center;
		gap: 0.65rem;
		white-space: nowrap;
		flex-shrink: 0;
	}

	.logo-text {
		font-family: var(--font-display);
		font-size: 1.35rem;
		letter-spacing: 0.04em;
	}

	.logo-text .accent {
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

	.nav-right {
		display: flex;
		align-items: center;
		gap: 1.25rem;
		flex-shrink: 0;
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

	.action i {
		font-size: 1.15rem;
		line-height: 1;
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
		font-size: 1.2rem;
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

		.action i {
			font-size: 1.25rem;
		}
	}

	@media (max-width: 640px) {
		.logo-text {
			display: none;
		}
	}
</style>

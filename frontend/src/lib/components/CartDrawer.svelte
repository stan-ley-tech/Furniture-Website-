<script lang="ts">
	import { cart, cartTotal } from '$lib/cart';
	import { cartOpen } from '$lib/ui';

	function close() {
		cartOpen.set(false);
	}

	function handleKeydown(e: KeyboardEvent) {
		if (e.key === 'Escape') close();
	}

	const priceFormatter = new Intl.NumberFormat('en-KE', {
		style: 'currency',
		currency: 'KES',
		maximumFractionDigits: 0
	});
</script>

<svelte:window onkeydown={handleKeydown} />

{#if $cartOpen}
	<div class="backdrop" onclick={close} role="presentation"></div>

	<div class="drawer" role="dialog" aria-label="Shopping cart" aria-modal="true">
		<div class="drawer-header">
			<h2>Your Cart</h2>
			<button class="close-btn" onclick={close} aria-label="Close cart">
				<i class="fa-solid fa-xmark"></i>
			</button>
		</div>

		{#if $cart.length === 0}
			<div class="empty">
				<p>Your cart is empty.</p>
				<a href="/shop" class="btn btn-solid" onclick={close}>Shop the Collection</a>
			</div>
		{:else}
			<ul class="items">
				{#each $cart as item (item.slug)}
					<li>
						<img src={item.image} alt={item.name} />
						<div class="item-info">
							<a href="/products/{item.slug}" onclick={close}>{item.name}</a>
							<p class="item-price">{priceFormatter.format(item.price)}</p>
							<div class="qty-row">
								<button
									aria-label="Decrease quantity"
									onclick={() => cart.setQuantity(item.slug, item.quantity - 1)}>&minus;</button
								>
								<span>{item.quantity}</span>
								<button
									aria-label="Increase quantity"
									onclick={() => cart.setQuantity(item.slug, item.quantity + 1)}>+</button
								>
								<button class="remove" onclick={() => cart.remove(item.slug)}>Remove</button>
							</div>
						</div>
					</li>
				{/each}
			</ul>

			<div class="drawer-footer">
				<div class="subtotal">
					<span>Subtotal</span>
					<span>{priceFormatter.format($cartTotal)}</span>
				</div>
				<a class="btn btn-solid checkout" href="/checkout" onclick={close}>Checkout</a>
			</div>
		{/if}
	</div>
{/if}

<style>
	.backdrop {
		position: fixed;
		inset: 0;
		background: rgba(20, 16, 12, 0.45);
		z-index: 40;
	}

	.drawer {
		position: fixed;
		top: 0;
		right: 0;
		bottom: 0;
		width: min(24rem, 100%);
		background: var(--color-surface);
		z-index: 41;
		display: flex;
		flex-direction: column;
		box-shadow: -8px 0 24px rgba(20, 16, 12, 0.15);
	}

	.drawer-header {
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding: 1.5rem;
		border-bottom: 1px solid var(--color-border);
	}

	.drawer-header h2 {
		font-size: 1.1rem;
	}

	.close-btn {
		background: none;
		border: none;
		font-size: 1.1rem;
		color: var(--color-text);
	}

	.empty {
		padding: 2rem 1.5rem;
		text-align: center;
	}

	.empty p {
		color: var(--color-text-muted);
		margin-bottom: 1.25rem;
	}

	.items {
		list-style: none;
		margin: 0;
		padding: 0;
		overflow-y: auto;
		flex: 1;
	}

	.items li {
		display: flex;
		gap: 1rem;
		padding: 1.25rem 1.5rem;
		border-bottom: 1px solid var(--color-border);
	}

	.items img {
		width: 5rem;
		height: 5rem;
		object-fit: cover;
		flex-shrink: 0;
	}

	.item-info {
		flex: 1;
		min-width: 0;
	}

	.item-info a {
		font-size: 0.9rem;
		font-weight: 500;
		color: var(--color-text);
		display: block;
		margin-bottom: 0.3rem;
	}

	.item-price {
		font-size: 0.85rem;
		color: var(--color-text-muted);
		margin-bottom: 0.6rem;
	}

	.qty-row {
		display: flex;
		align-items: center;
		gap: 0.6rem;
	}

	.qty-row button {
		background: none;
		border: 1px solid var(--color-border);
		width: 1.6rem;
		height: 1.6rem;
		font-size: 0.9rem;
		color: var(--color-text);
		line-height: 1;
	}

	.qty-row span {
		font-size: 0.85rem;
		min-width: 1.2rem;
		text-align: center;
	}

	.qty-row .remove {
		border: none;
		margin-left: auto;
		font-size: 0.75rem;
		text-decoration: underline;
		color: var(--color-text-muted);
		width: auto;
		height: auto;
	}

	.drawer-footer {
		padding: 1.5rem;
		border-top: 1px solid var(--color-border);
	}

	.subtotal {
		display: flex;
		justify-content: space-between;
		font-size: 0.95rem;
		margin-bottom: 1rem;
	}

	.checkout {
		display: flex;
		width: 100%;
	}
</style>

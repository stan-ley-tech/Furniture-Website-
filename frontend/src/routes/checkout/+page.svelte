<script lang="ts">
	import { cart, cartTotal } from '$lib/cart';

	let name = $state('');
	let email = $state('');
	let address = $state('');
	let submitted = $state(false);

	const priceFormatter = new Intl.NumberFormat('en-KE', {
		style: 'currency',
		currency: 'KES',
		maximumFractionDigits: 0
	});

	function handleSubmit(e: SubmitEvent) {
		e.preventDefault();
		submitted = true;
		cart.clear();
	}
</script>

<svelte:head>
	<title>Checkout &mdash; Elite Wood Furniture</title>
</svelte:head>

<section class="container checkout">
	{#if submitted}
		<div class="confirmation">
			<p class="eyebrow">Checkout</p>
			<h1>Order Received</h1>
			<p>
				Thanks{name ? `, ${name}` : ''} &mdash; this is a demo storefront, so no payment was
				processed, but in production we'd email a confirmation to {email || 'your inbox'} and
				start preparing your order.
			</p>
			<a class="btn btn-solid" href="/shop">Continue Shopping</a>
		</div>
	{:else if $cart.length === 0}
		<div class="confirmation">
			<p class="eyebrow">Checkout</p>
			<h1>Your Cart Is Empty</h1>
			<p>Add something from the collection before checking out.</p>
			<a class="btn btn-solid" href="/shop">Shop the Collection</a>
		</div>
	{:else}
		<div class="checkout-grid">
			<div>
				<p class="eyebrow">Checkout</p>
				<h1>Shipping Details</h1>
				<form onsubmit={handleSubmit}>
					<label>
						Full Name
						<input type="text" bind:value={name} required />
					</label>
					<label>
						Email Address
						<input type="email" bind:value={email} required />
					</label>
					<label>
						Delivery Address
						<textarea rows="3" bind:value={address} required></textarea>
					</label>
					<button class="btn btn-solid" type="submit">Place Order</button>
				</form>
			</div>

			<div class="summary">
				<h2>Order Summary</h2>
				<ul>
					{#each $cart as item (item.slug)}
						<li>
							<img src={item.image} alt={item.name} />
							<div>
								<p class="name">{item.name}</p>
								<p class="qty">Qty {item.quantity}</p>
							</div>
							<p class="line-price">{priceFormatter.format(item.price * item.quantity)}</p>
						</li>
					{/each}
				</ul>
				<div class="total">
					<span>Total</span>
					<span>{priceFormatter.format($cartTotal)}</span>
				</div>
			</div>
		</div>
	{/if}
</section>

<style>
	.checkout {
		padding: 4rem var(--gutter) 6rem;
	}

	.confirmation {
		max-width: 28rem;
	}

	.confirmation h1 {
		font-size: clamp(1.6rem, 3vw, 2rem);
		margin: 0.5rem 0 1rem;
	}

	.confirmation p:not(.eyebrow) {
		color: var(--color-text-muted);
		line-height: 1.65;
		margin-bottom: 1.75rem;
	}

	.checkout-grid {
		display: grid;
		grid-template-columns: 1.2fr 1fr;
		gap: 3.5rem;
	}

	h1 {
		font-size: clamp(1.6rem, 3vw, 2rem);
		margin: 0.5rem 0 1.75rem;
	}

	form {
		display: flex;
		flex-direction: column;
		gap: 1.25rem;
		max-width: 26rem;
	}

	label {
		display: flex;
		flex-direction: column;
		gap: 0.5rem;
		font-size: 0.85rem;
		color: var(--color-text-muted);
	}

	input,
	textarea {
		font-family: var(--font-body);
		font-size: 0.95rem;
		padding: 0.75rem 0.9rem;
		border: 1px solid var(--color-border);
		background: var(--color-surface);
		color: var(--color-text);
		resize: vertical;
	}

	button[type='submit'] {
		margin-top: 0.5rem;
		align-self: flex-start;
	}

	.summary {
		background: var(--color-bg-alt);
		padding: 2rem;
		height: fit-content;
	}

	.summary h2 {
		font-size: 1.05rem;
		margin-bottom: 1.25rem;
	}

	.summary ul {
		list-style: none;
		margin: 0 0 1.25rem;
		padding: 0;
	}

	.summary li {
		display: flex;
		align-items: center;
		gap: 0.85rem;
		padding: 0.75rem 0;
		border-bottom: 1px solid var(--color-border);
	}

	.summary img {
		width: 3.5rem;
		height: 3.5rem;
		object-fit: cover;
		flex-shrink: 0;
	}

	.summary li div {
		flex: 1;
	}

	.name {
		font-size: 0.88rem;
		font-weight: 500;
	}

	.qty {
		font-size: 0.78rem;
		color: var(--color-text-muted);
		margin-top: 0.2rem;
	}

	.line-price {
		font-size: 0.85rem;
		color: var(--color-text-muted);
	}

	.total {
		display: flex;
		justify-content: space-between;
		font-size: 1.05rem;
		font-weight: 500;
		padding-top: 0.5rem;
	}

	@media (max-width: 720px) {
		.checkout-grid {
			grid-template-columns: 1fr;
		}
	}
</style>

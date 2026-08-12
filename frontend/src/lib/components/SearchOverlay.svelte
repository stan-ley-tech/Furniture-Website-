<script lang="ts">
	import { getProducts, type Product } from '$lib/api';
	import { searchOpen } from '$lib/ui';

	let query = $state('');
	let allProducts: Product[] = $state([]);
	let loaded = $state(false);
	let inputEl: HTMLInputElement | undefined = $state();

	const results = $derived(
		query.trim().length === 0
			? []
			: allProducts
					.filter((p) => {
						const q = query.trim().toLowerCase();
						return (
							p.name.toLowerCase().includes(q) ||
							p.category.toLowerCase().includes(q) ||
							p.description.toLowerCase().includes(q)
						);
					})
					.slice(0, 6)
	);

	const priceFormatter = new Intl.NumberFormat('en-KE', {
		style: 'currency',
		currency: 'KES',
		maximumFractionDigits: 0
	});

	async function ensureLoaded() {
		if (loaded) return;
		allProducts = await getProducts();
		loaded = true;
	}

	function close() {
		searchOpen.set(false);
		query = '';
	}

	function handleKeydown(e: KeyboardEvent) {
		if (e.key === 'Escape') close();
	}

	$effect(() => {
		if ($searchOpen) {
			ensureLoaded();
			inputEl?.focus();
		}
	});
</script>

<svelte:window onkeydown={handleKeydown} />

{#if $searchOpen}
	<div class="backdrop" onclick={close} role="presentation"></div>

	<div class="panel" role="dialog" aria-label="Search products" aria-modal="true">
		<div class="container search-bar">
			<i class="fa-solid fa-magnifying-glass"></i>
			<input
				bind:this={inputEl}
				bind:value={query}
				type="text"
				placeholder="Search dining tables, chairs, beds..."
			/>
			<button class="close-btn" onclick={close} aria-label="Close search">
				<i class="fa-solid fa-xmark"></i>
			</button>
		</div>

		{#if query.trim().length > 0}
			<div class="container results">
				{#if results.length > 0}
					{#each results as product (product.id)}
						<a class="result" href="/products/{product.slug}" onclick={close}>
							<img src={product.image} alt={product.name} />
							<div>
								<p class="name">{product.name}</p>
								<p class="category">{product.category}</p>
							</div>
							<p class="price">{priceFormatter.format(product.price)}</p>
						</a>
					{/each}
				{:else}
					<p class="empty">No pieces match &ldquo;{query}&rdquo;.</p>
				{/if}
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

	.panel {
		position: fixed;
		top: 0;
		left: 0;
		right: 0;
		background: var(--color-surface);
		z-index: 41;
		box-shadow: 0 8px 24px rgba(20, 16, 12, 0.15);
		max-height: 85vh;
		overflow-y: auto;
	}

	.search-bar {
		display: flex;
		align-items: center;
		gap: 1rem;
		padding: 1.5rem var(--gutter);
		border-bottom: 1px solid var(--color-border);
	}

	.search-bar i {
		color: var(--color-text-muted);
		font-size: 1.1rem;
	}

	.search-bar input {
		flex: 1;
		border: none;
		outline: none;
		background: none;
		font-family: var(--font-body);
		font-size: 1.1rem;
		color: var(--color-text);
	}

	.close-btn {
		background: none;
		border: none;
		font-size: 1.2rem;
		color: var(--color-text);
	}

	.results {
		padding: 1rem var(--gutter) 2rem;
	}

	.result {
		display: flex;
		align-items: center;
		gap: 1rem;
		padding: 0.85rem 0;
		border-bottom: 1px solid var(--color-border);
	}

	.result img {
		width: 3.5rem;
		height: 3.5rem;
		object-fit: cover;
		flex-shrink: 0;
	}

	.result div {
		flex: 1;
	}

	.name {
		font-size: 0.92rem;
		font-weight: 500;
		color: var(--color-text);
	}

	.category {
		font-size: 0.78rem;
		color: var(--color-text-muted);
		margin-top: 0.2rem;
	}

	.price {
		font-size: 0.88rem;
		color: var(--color-text-muted);
	}

	.empty {
		color: var(--color-text-muted);
		padding: 1.5rem 0;
	}
</style>

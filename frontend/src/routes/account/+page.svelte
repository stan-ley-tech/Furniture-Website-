<script lang="ts">
	let mode: 'sign-in' | 'create' = $state('sign-in');
	let email = $state('');
	let password = $state('');
	let name = $state('');
	let submitted = $state(false);

	function handleSubmit(e: SubmitEvent) {
		e.preventDefault();
		submitted = true;
	}
</script>

<svelte:head>
	<title>Account &mdash; Elite Wood Furniture</title>
	<meta name="description" content="Sign in or create an Elite Wood Furniture account." />
</svelte:head>

<section class="container account">
	{#if submitted}
		<div class="confirmation">
			<p class="eyebrow">Account</p>
			<h1>You're Signed In</h1>
			<p>
				This is a demo storefront, so accounts aren't wired up to a real backend yet &mdash; but
				in production this is where your order history and saved details would live.
			</p>
			<a class="btn btn-solid" href="/shop">Continue Shopping</a>
		</div>
	{:else}
		<div class="account-box">
			<div class="tabs">
				<button class:active={mode === 'sign-in'} onclick={() => (mode = 'sign-in')}
					>Sign In</button
				>
				<button class:active={mode === 'create'} onclick={() => (mode = 'create')}
					>Create Account</button
				>
			</div>

			<p class="eyebrow">Account</p>
			<h1>{mode === 'sign-in' ? 'Welcome Back' : 'Create Your Account'}</h1>

			<form onsubmit={handleSubmit}>
				{#if mode === 'create'}
					<label>
						Full Name
						<input type="text" bind:value={name} required />
					</label>
				{/if}
				<label>
					Email Address
					<input type="email" bind:value={email} required />
				</label>
				<label>
					Password
					<input type="password" bind:value={password} required minlength="8" />
				</label>
				<button class="btn btn-solid" type="submit"
					>{mode === 'sign-in' ? 'Sign In' : 'Create Account'}</button
				>
			</form>
		</div>
	{/if}
</section>

<style>
	.account {
		max-width: 28rem;
		padding: 4rem var(--gutter) 6rem;
	}

	.tabs {
		display: flex;
		gap: 1.5rem;
		margin-bottom: 2rem;
		border-bottom: 1px solid var(--color-border);
	}

	.tabs button {
		background: none;
		border: none;
		padding: 0 0 0.85rem;
		font-size: 0.8rem;
		letter-spacing: 0.06em;
		text-transform: uppercase;
		color: var(--color-text-muted);
		border-bottom: 2px solid transparent;
		margin-bottom: -1px;
	}

	.tabs button.active {
		color: var(--color-text);
		border-color: var(--color-accent);
	}

	h1 {
		font-size: clamp(1.6rem, 3vw, 2rem);
		margin: 0.5rem 0 1.75rem;
	}

	form {
		display: flex;
		flex-direction: column;
		gap: 1.25rem;
	}

	label {
		display: flex;
		flex-direction: column;
		gap: 0.5rem;
		font-size: 0.85rem;
		color: var(--color-text-muted);
	}

	input {
		font-family: var(--font-body);
		font-size: 0.95rem;
		padding: 0.75rem 0.9rem;
		border: 1px solid var(--color-border);
		background: var(--color-surface);
		color: var(--color-text);
	}

	button[type='submit'] {
		margin-top: 0.5rem;
	}

	.confirmation p:not(.eyebrow) {
		color: var(--color-text-muted);
		line-height: 1.65;
		margin: 1rem 0 1.75rem;
	}
</style>

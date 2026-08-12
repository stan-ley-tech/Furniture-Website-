<script lang="ts">
	let name = $state('');
	let email = $state('');
	let message = $state('');
	let submitted = $state(false);

	function handleSubmit(e: SubmitEvent) {
		e.preventDefault();
		submitted = true;
	}
</script>

<svelte:head>
	<title>Free Design Consultation &mdash; Elite Wood Furniture</title>
	<meta
		name="description"
		content="Tell us about your space and one of our designers will help you plan it."
	/>
</svelte:head>

<section class="container consultation">
	<div class="intro">
		<p class="eyebrow">Design Consultation</p>
		<h1>Tell Us About Your Space</h1>
		<p class="lede">
			Share a few details and one of our designers will follow up with furniture and layout
			suggestions for your room &mdash; free of charge, no obligation.
		</p>
	</div>

	{#if submitted}
		<div class="confirmation">
			<h2>Thank you</h2>
			<p>We've received your request and will be in touch within two business days.</p>
		</div>
	{:else}
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
				Tell us about your space
				<textarea rows="5" bind:value={message} placeholder="Room type, style, budget..."
				></textarea>
			</label>
			<button class="btn btn-solid" type="submit">Request Consultation</button>
		</form>
	{/if}
</section>

<style>
	.consultation {
		max-width: 40rem;
		padding: 4rem var(--gutter) 6rem;
	}

	.intro h1 {
		font-size: clamp(1.8rem, 3.5vw, 2.4rem);
		margin: 0.5rem 0 1rem;
	}

	.intro .lede {
		color: var(--color-text-muted);
		line-height: 1.6;
		margin-bottom: 2.5rem;
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

	button {
		margin-top: 0.5rem;
		align-self: flex-start;
	}

	.confirmation {
		padding: 2.5rem;
		background: var(--color-bg-alt);
		border: 1px solid var(--color-border);
	}

	.confirmation h2 {
		font-size: 1.3rem;
		margin-bottom: 0.5rem;
	}

	.confirmation p {
		color: var(--color-text-muted);
	}
</style>

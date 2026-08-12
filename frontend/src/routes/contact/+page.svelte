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
	<title>Contact Us &mdash; Elite Wood Furniture</title>
	<meta name="description" content="Get in touch with Elite Wood Furniture." />
</svelte:head>

<section class="container contact">
	<div class="contact-info">
		<p class="eyebrow">Contact Us</p>
		<h1>We're Happy to Help</h1>
		<p class="lede">
			Questions about an order, a piece in the collection, or a custom build &mdash; reach out and
			we'll get back to you within one business day.
		</p>

		<dl>
			<div>
				<dt>Email</dt>
				<dd><a href="mailto:hello@elitewoodfurniture.co.ke">hello@elitewoodfurniture.co.ke</a></dd>
			</div>
			<div>
				<dt>Phone</dt>
				<dd><a href="tel:+254700000000">+254 700 000 000</a></dd>
			</div>
			<div>
				<dt>Showroom</dt>
				<dd>Karen Road, Nairobi, Kenya</dd>
			</div>
			<div>
				<dt>Hours</dt>
				<dd>Mon&ndash;Sat, 9am&ndash;6pm</dd>
			</div>
		</dl>
	</div>

	<div class="contact-form">
		{#if submitted}
			<div class="confirmation">
				<h2>Message sent</h2>
				<p>Thanks for reaching out &mdash; we'll reply within one business day.</p>
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
					Message
					<textarea rows="5" bind:value={message} required></textarea>
				</label>
				<button class="btn btn-solid" type="submit">Send Message</button>
			</form>
		{/if}
	</div>
</section>

<style>
	.contact {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 3.5rem;
		padding: 4rem var(--gutter) 6rem;
	}

	.contact-info h1 {
		font-size: clamp(1.8rem, 3.5vw, 2.4rem);
		margin: 0.5rem 0 1rem;
	}

	.contact-info .lede {
		color: var(--color-text-muted);
		line-height: 1.6;
		margin-bottom: 2rem;
	}

	dl div {
		padding: 0.85rem 0;
		border-bottom: 1px solid var(--color-border);
	}

	dt {
		font-size: 0.72rem;
		letter-spacing: 0.08em;
		text-transform: uppercase;
		color: var(--color-text-muted);
		margin-bottom: 0.3rem;
	}

	dd {
		margin: 0;
		font-size: 0.95rem;
	}

	dd a {
		color: var(--color-text);
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

	@media (max-width: 720px) {
		.contact {
			grid-template-columns: 1fr;
		}
	}
</style>

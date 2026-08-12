<script lang="ts">
	const faqs = [
		{
			q: 'What wood do you use?',
			a: 'Mostly white oak, walnut, ash, and cedar for outdoor pieces — always solid hardwood, never particleboard or MDF.'
		},
		{
			q: 'How long does delivery take?',
			a: 'In-stock pieces typically arrive within a week via white-glove delivery. Made-to-order pieces are quoted a delivery window at purchase.'
		},
		{
			q: 'Do you deliver outside Nairobi?',
			a: 'Yes — delivery fees outside Nairobi are calculated at checkout based on distance.'
		},
		{
			q: 'Can I customize dimensions or finish?',
			a: 'Many pieces can be adjusted in size or finish. Reach out through our consultation form and we’ll confirm what’s possible for the piece you have in mind.'
		},
		{
			q: 'What is your return policy?',
			a: 'You have 14 days from delivery to request a return on unused items in original condition. See our Shipping & Returns page for full details.'
		},
		{
			q: 'Is my furniture covered by a warranty?',
			a: 'Yes — every piece includes a 5-year structural warranty against defects in materials and joinery. See our Warranty page for details.'
		}
	];
</script>

<svelte:head>
	<title>FAQ &mdash; Elite Wood Furniture</title>
	<meta name="description" content="Frequently asked questions about Elite Wood Furniture." />
</svelte:head>

<section class="simple-page">
	<p class="eyebrow">Support</p>
	<h1>Frequently Asked Questions</h1>

	<div class="faq-list">
		{#each faqs as item}
			<details>
				<summary>{item.q}</summary>
				<p>{item.a}</p>
			</details>
		{/each}
	</div>

	<p class="footer-note">
		Didn't find your answer? <a href="/contact">Contact us</a> directly.
	</p>
</section>

<style>
	.faq-list {
		margin-top: 1.5rem;
	}

	details {
		border-bottom: 1px solid var(--color-border);
		padding: 1.1rem 0;
	}

	summary {
		cursor: pointer;
		font-weight: 500;
		font-size: 0.98rem;
		list-style: none;
	}

	summary::-webkit-details-marker {
		display: none;
	}

	summary::before {
		content: '+ ';
		color: var(--color-accent);
		font-weight: 700;
	}

	details[open] summary::before {
		content: '\2212 ';
	}

	details p {
		margin-top: 0.75rem;
		margin-bottom: 0;
	}

	.footer-note {
		margin-top: 2rem;
	}
</style>

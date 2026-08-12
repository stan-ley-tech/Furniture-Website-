<script lang="ts">
	let { size = 40 }: { size?: number } = $props();
</script>

<svg viewBox="0 0 120 120" width={size} height={size} aria-hidden="true">
	<circle cx="60" cy="60" r="57" fill="var(--color-bg)" />
	<circle cx="60" cy="60" r="52" fill="none" stroke="var(--color-accent)" stroke-width="4" />
	<text
		x="60"
		y="78"
		text-anchor="middle"
		font-family="Georgia, 'Times New Roman', serif"
		font-weight="700"
		font-size="54"
		fill="var(--color-text)">EW</text
	>
</svg>

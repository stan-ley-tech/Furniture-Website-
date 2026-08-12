<a
	class="whatsapp-btn"
	href="https://wa.me/254700000000"
	target="_blank"
	rel="noopener noreferrer"
	aria-label="Chat with us on WhatsApp"
>
	<i class="fa-brands fa-whatsapp"></i>
</a>

<style>
	.whatsapp-btn {
		position: fixed;
		right: 1.5rem;
		bottom: 1.5rem;
		z-index: 15;
		width: 3.4rem;
		height: 3.4rem;
		display: flex;
		align-items: center;
		justify-content: center;
		background: #25d366;
		color: #ffffff;
		border-radius: 50%;
		font-size: 1.7rem;
		box-shadow: 0 4px 14px rgba(20, 16, 12, 0.3);
		transition:
			transform 0.2s ease,
			box-shadow 0.2s ease;
	}

	.whatsapp-btn:hover {
		transform: scale(1.06);
		box-shadow: 0 6px 18px rgba(20, 16, 12, 0.35);
	}

	@media (max-width: 640px) {
		.whatsapp-btn {
			right: 1rem;
			bottom: 1rem;
			width: 3.1rem;
			height: 3.1rem;
			font-size: 1.55rem;
		}
	}
</style>

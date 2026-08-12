export type Category = {
	slug: string;
	name: string;
	description: string;
	image: string;
};

export const categories: Category[] = [
	{
		slug: 'living-room',
		name: 'Living Room',
		description: 'Sofas, lounge chairs, and everyday seating built to last.',
		image: '/images/categories/living-room.jpg'
	},
	{
		slug: 'dining-room',
		name: 'Dining Room',
		description: 'Tables and seating for gathering, built from solid hardwood.',
		image: '/images/categories/dining-room.jpg'
	},
	{
		slug: 'bedroom',
		name: 'Bedroom',
		description: 'Beds and bedroom furniture crafted for a calmer room.',
		image: '/images/categories/bedroom.jpg'
	},
	{
		slug: 'storage',
		name: 'Storage',
		description: 'Shelving, sideboards, and cabinetry with real joinery.',
		image: '/images/products/haven-walnut-bookshelf.jpg'
	},
	{
		slug: 'outdoor',
		name: 'Outdoor',
		description: 'Weather-ready pieces built from naturally durable wood.',
		image: '/images/categories/outdoor.jpg'
	}
];

export function getCategory(slug: string): Category | undefined {
	return categories.find((c) => c.slug === slug);
}

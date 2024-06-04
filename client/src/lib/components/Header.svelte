<script lang="ts">
	import { page } from '$app/stores';
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu';
	import ThemeToggle from '$lib/components/ThemeToggle.svelte';
	import HealthiconsUiMenuOutline from '~icons/healthicons/ui-menu-outline';

	const routes = [
		{
			name: 'About',
			path: '/about'
		},
		{
			name: 'Contact',
			path: '/contact'
		},
		{
			name: 'Support',
			path: '/support'
		}
	];

	function isActive(path: string): boolean {
		return Boolean($page.url.pathname === path || $page.url.pathname.startsWith(path));
	}
</script>

<header class="flex items-center justify-between px-6 py-4 dark:bg-muted md:px-8">
	<a href="/" class="font-serif text-2xl font-bold italic md:hidden">
		<span>Rizz Up</span>
	</a>
	<nav class="hidden items-center justify-center space-x-4 md:flex">
		<a href="/" class="mr-4 font-serif text-2xl font-bold italic">
			<span>Rizz Up</span>
		</a>
		{#each routes as route}
			<div
				aria-current={isActive(route.path) ? 'page' : undefined}
				class="font-serif text-lg italic underline-offset-4 transition duration-100 ease-in-out hover:underline"
			>
				<a href={route.path}>{route.name}</a>
			</div>
		{/each}
	</nav>
	<div class="flex h-full space-x-4 md:hidden">
		<ThemeToggle outline={false} />
		<DropdownMenu.Root>
			<DropdownMenu.Trigger>
				<HealthiconsUiMenuOutline />
			</DropdownMenu.Trigger>
			<DropdownMenu.Content>
				<DropdownMenu.Group>
					{#each routes as route}
						<DropdownMenu.Item>
							<a href={route.path}>{route.name}</a>
						</DropdownMenu.Item>
					{/each}
				</DropdownMenu.Group>
			</DropdownMenu.Content>
		</DropdownMenu.Root>
	</div>
	<div class="hidden md:flex">
		<ThemeToggle />
	</div>
</header>

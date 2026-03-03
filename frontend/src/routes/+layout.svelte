<script lang="ts">
  import 'noph-ui/defaultTheme'
  import '../app.css'
  import '@fontsource/material-symbols-outlined';
  import '@fontsource/roboto-flex';

	import favicon from '$lib/assets/favicon.svg';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

{@render children()}

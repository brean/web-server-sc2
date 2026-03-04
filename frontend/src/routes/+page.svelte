<script lang="ts">
  import SCCom from "$lib/com/SCCom";
  import { uiState } from "$lib/state/ui_state.svelte";
  import { Button, Card } from "noph-ui";
  import { onMount } from "svelte";

  onMount(() => {
    if (!uiState.com) {
      uiState.com = new SCCom();
    }
    uiState.games = [
      {
        bot_name: 'test_bot',
        opponent_name: 'pc_medium',
        game_id: '1234567890',
        map: 'Abyssal Reef',
        started: new Date(2026, 1, 1, 12, 13, 14),
        finished: new Date(2026, 1, 1, 12, 13, 16)
      }
    ]
  })

    let items = $state([
    { id: 1, title: 'Project Alpha', desc: 'A Svelte 5 starter template.' },
    { id: 2, title: 'Project Beta', desc: 'Responsive UI components.' },
    { id: 3, title: 'Project Gamma', desc: 'Built with noph-ui and Runes.' },
    { id: 4, title: 'Project Delta', desc: 'Scalable grid layouts.' }
  ]);
</script>
<h4>Existing games</h4>

<div class="card-grid">
{#each uiState.games as game}
<Card type="button"
  variant="elevated"
  headline={game.game_name ? game.game_name : game.game_id.substring(game.game_id.length-6)}
  supportingText={game.bot_name + ' vs ' + game.opponent_name + ' on ' + game.map}
>
</Card>
{/each}
</div>


<br />

<Button>Start new Game!</Button>

<style>
  .cards {
    display: grid;
    gap: 0.5rem;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    padding: 2rem;
  }

  * {
    box-sizing: border-box;
  }

  .card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1.5rem;
    padding: 1rem;
    width: 100%;
  }

  /* Optional: Add a max-width for very large desktops to prevent cards 
    from becoming too wide if only a few exist in a row */
  :global(.custom-card) {
    max-width: 450px; 
    justify-self: center;
    width: 100%;
  }
</style>
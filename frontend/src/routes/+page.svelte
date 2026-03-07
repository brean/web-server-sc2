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

  :global(.custom-card) {
    max-width: 450px; 
    justify-self: center;
    width: 100%;
  }
</style>
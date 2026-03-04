<script lang="ts">
  import SCCom from "$lib/com/SCCom";
  import { uiState } from "$lib/state/ui_state.svelte";
  import { Button, Card } from "noph-ui";
  import { onMount } from "svelte";

  onMount(() => {
    if (!uiState.com) {
      uiState.com = new SCCom();
    }
  })
</script>
<h4>Existing games</h4>

{#each uiState.games as game}
<Card about={game.game_id}>
</Card>
{/each}


<Button>Start new Game!</Button>
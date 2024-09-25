<script lang="ts">
  import IGame from '$lib/model/IGameState';
  import Button, { Label } from '@smui/button';
  import Card, { Content, Actions } from '@smui/card';
  import sc_com from '$lib/store/sc_com';
  import LayoutGrid, { Cell } from '@smui/layout-grid';
  import { onMount } from 'svelte';
  import SCCom from '$lib/com/SCCom';
  import games from '$lib/store/games';
  import Select, { Option } from '@smui/select';

  // TODO: fetch data from previous runs
  // TODO: websocket to get live data and show data on canvas (as well as state machine, ...)
  let map: string = '';

  onMount(() => {
    if (!$sc_com) {
      $sc_com = new SCCom();
      // TODO: send start of bot $sc_com.send('');
    }
  })

  function start(game_id: string) {
    $sc_com?.send(JSON.stringify({
      type: 'start_game',
      game_id, map
    }))
  }

</script>

Game streams:

{#if ($games.length == 0)}
  No games playing
{:else}
  <LayoutGrid>
    {#each $games as game}
    <Cell>
      <div class="card-container">
        <Card>
          <Content>
            {game.game_id}<br />
            {game.bot_name}<br />
            <Select bind:value={map} label="Map">
              {#each game.maps as map_name}
                <Option value={map_name}>{map_name}</Option>
              {/each}
            </Select>
          </Content>
          <Actions>
            {#if !game.started}
            <Button on:click={() => start(game.game_id)}>
              <Label>start</Label>
            </Button>
            {/if}
          </Actions>
        </Card>
      </div>
    </Cell>
    {/each}
  </LayoutGrid>
{/if}

<script lang="ts">
  import IGame from '$lib/model/IGame';
  import Button, { Label } from '@smui/button';
  import Card, { Content, Actions } from '@smui/card';
  import sc_com from '$lib/store/sc_com';
  import LayoutGrid, { Cell } from '@smui/layout-grid';
  import { onMount } from 'svelte';
  import SCCom from '$lib/com/SCCom';

  const games: IGame[] = [
    {
      name: "A game that has been played in the past"
    },
    {
      name: 'game 2'
    }
  ]

  // TODO: fetch data from previous runs
  // TODO: websocket to get live data and show data on canvas (as well as state machine, ...)

  onMount(() => {
    if (!$sc_com) {
      $sc_com = new SCCom();
      // TODO: send start of bot $sc_com.send('');
    }
  })

</script>

Game streams:

<LayoutGrid>
  {#each games as game}
  <Cell>
    <div class="card-container">
      <Card>
        <Content>{game.name}</Content>
        <Actions>
          <Button>
            <Label>delete</Label>
          </Button>
          <Button>
            <Label>view</Label>
          </Button>
        </Actions>
      </Card>
    </div>
  </Cell>
  {/each}
</LayoutGrid>

Game recordings:


<LayoutGrid>
  {#each games as game}
  <Cell>
    <div class="card-container">
      <Card>
        <Content>{game.name}</Content>
        <Actions>
          <Button>
            <Label>delete</Label>
          </Button>
          <Button>
            <Label>view</Label>
          </Button>
        </Actions>
      </Card>
    </div>
  </Cell>
  {/each}
</LayoutGrid>
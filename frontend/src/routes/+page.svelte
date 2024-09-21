<script lang="ts">
  import IGame from '$lib/model/IGame';
  import Button, { Label } from '@smui/button';
  import Card, { Content, Actions } from '@smui/card';
  import LayoutGrid, { Cell } from '@smui/layout-grid';

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
<script lang="ts">
  import Button, { Label } from '@smui/button';
  import Card, { Content } from '@smui/card';
  import Actions from '@smui/card/src/Actions.svelte';
  import LayoutGrid from '@smui/layout-grid';
  import Cell from '@smui/layout-grid/src/Cell.svelte';

  const games = [{}, {}, {}, {}]
</script>

<LayoutGrid>
  {#each games as game}
  <Cell>
    <div class="card-container">
      <Card>
        <Content>A game that has been played in the past.</Content>
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

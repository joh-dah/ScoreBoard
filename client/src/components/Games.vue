<template>
    <div class="container">
        <div class="row">
            <div class="col-sm-10">
                <h1>Games</h1>
                <hr><br><br>
                <button class="btn btn-outline-primary fancy-button" @click="newGame()">New Game</button>
                <br><br>
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th scope="col">Team 1</th>
                            <th scope="col">Team 2</th>
                            <th scope="col">Game ID</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(game, index) in games" :key="index">
                            <td>{{ game.score_1 }}</td>
                            <td>{{ game.score_2 }}</td>
                            <td>{{ game.gameId }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>
  
<script>
import axios from 'axios';

export default {
    data() {
        return {
            games: [],
        };
    },
    methods: {
        getGames() {
            const path = 'http://localhost:5001/games';
            axios.get(path)
                .then((res) => {
                    this.games = res.data;
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        newGame() {
            // create new game and add to database. Go to game page
            const path = 'http://localhost:5001/games';
            axios.post(path)
                .then((res) => {
                    this.$router.push({ name: 'scoreboard', params: { gameId: res.data.gameId } });
                })
                .catch((error) => {
                    console.error(error);
                });
        },
    },
    created() {
        this.getGames();
    },
};
</script>
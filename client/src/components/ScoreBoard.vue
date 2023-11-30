<template>
  <div class="container">
    <div class="row score-container">
      <div class="col-md-12 text-center">
        <h3>Scores</h3>
        <div class="score">{{ score_1 }} : {{ score_2 }}</div>
        <button class="btn btn-outline-primary fancy-button" @click="updateScore('score_1', 1)">+</button>
        <button class="btn btn-outline-primary fancy-button" @click="updateScore('score_1', -1)">-</button>
        <button class="btn btn-outline-primary fancy-button" @click="updateScore('score_2', 1)"
          style="margin-left: 20px;">+</button>
        <button class="btn btn-outline-primary fancy-button" @click="updateScore('score_2', -1)">-</button>
      </div>
    </div>
    <div class="row" style="margin-top: 20px;">
      <button class="btn btn-outline-primary fancy-button" @click="endGame()">End Game</button>
    </div>
  </div>
</template>



<script>
import axios from 'axios';

export default {
  data() {
    return {
      score_1: 0,
      score_2: 0,
      gameId: this.$route.params.gameId,
    };
  },
  methods: {
    getScore() {
      //const path = 'http://10.107.57.85:5000/scoreboard';
      const path = 'http://localhost:5001/games/' + this.gameId;
      axios.get(path, {
        params: {
          gameId: this.gameId,
        },
      })
        .then((res) => {
          this.score_1 = res.data.score_1;
          this.score_2 = res.data.score_2;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    updateScore(team, value) {
      //const path = 'http://10.107.57.85:5000/scoreboard';
      const path = 'http://localhost:5001/games/' + this.gameId;
      const payload = {
        "score_1": this.score_1,
        "score_2": this.score_2,
        "gameId": this.gameId,
      };
      payload[team] += value;
      payload[team] = Math.max(0, payload[team]);
      axios.put(path, payload)
        .then(() => {
          this.getScore();
        })
        .catch((error) => {
          console.log(error);
          this.getScore();
        });
    },
    endGame() {
      this.$router.push({ name: 'games' });
    },
  },
  created() {
    this.getScore();
  },
};
</script>

  
<style scoped>
.score-container {
  text-align: center;
  margin-top: 50px;
}

.score {
  font-size: 3em;
  margin-bottom: 20px;
}

.fancy-button {
  margin: 0 10px;
  border-radius: 20px;
  padding: 10px 20px;
}
</style>
  
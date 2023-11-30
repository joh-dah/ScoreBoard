<template>
  <div class="container">
    <div class="row score-container">
      <div class="col-md-12 text-center">
        <h3>Scores</h3>
        <div class="score">{{ score_1 }} : {{ score_2 }}</div>
        <button class="btn btn-outline-primary fancy-button" @click="updateScore('score_1')">+</button>
        <button class="btn btn-outline-primary fancy-button" @click="updateScore('score_2')">+</button>
      </div>
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
      game_id: 1,
    };
  },
  methods: {
    initScore() {
      const path = 'http://10.107.57.85:5000/scoreboard';
      axios.post(path, {
        score_1: 0,
        score_2: 0,
      })
        .then((res) => {
          this.game_id = res.data.game_id;
          this.getScore();
        })
    },
    getScore() {
      const path = 'http://10.107.57.85:5000/scoreboard';
      axios.get(path, {
        params: {
          game_id: this.game_id,
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
    updateScore(team) {
      const path = 'http://10.107.57.85:5000/scoreboard';
      const payload = {
        "score_1": this.score_1,
        "score_2": this.score_2,
        "game_id": this.game_id,
      };
      payload[team] += 1;
      axios.put(path, payload)
        .then(() => {
          this.getScore();
        })
        .catch((error) => {
          console.log(error);
          this.getScore();
        });
    },
  },
  created() {
    this.initScore();
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
  
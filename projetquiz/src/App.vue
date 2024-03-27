<script setup>
import QuizItem from './components/QuizItem.vue';
</script>

<template>
  <QuizItem :quizs="quizs" />
</template>

<script>
export default {
  data() {
    return {
      quizs: [
        {'id': 1, 'name': "Quiz 1", 'questions': [{'intitule': "Question 1", "propositions": ["Oui", "Non", "Coucou"], "reponse": "Coucou"}, {'intitule': "Question 2", "propositions": ["Bonjour", "Oui", "Baguette", "Heyy"], "reponse": "Heyy"}]},
        {'id': 2, 'name': "Quiz 2", 'questions': [{'intitule': "Question 1", "propositions": ["Oui", "Test", "Coucou"], "reponse": "Test"}, {'intitule': "Question 2", "propositions": ["Oui", "Hehe", "Coucou"], "reponse": "Hehe"}, {'intitule': "Question 3", "propositions": ["Oui", "Non", "Coucou"], "reponse": "Non"}]},
        {'id': 3, 'name': "Quiz 3", 'questions': [{'intitule': "Question 1", "propositions": ["Oui", "Baguette", "Coucou"], "reponse": "Baguette"}]}
      ]
    };
  },
  components: {
    QuizItem
  }
};
</script>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>

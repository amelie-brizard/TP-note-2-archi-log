<script setup>
import QuizItem from './components/QuizItem.vue';
</script>

<template>
  <div>
    <QuizItem :quizs="quizs" />
  </div>
</template>

<script>
export default {
  data() {
    return {
      quizs: [
        {'id': 1, 'name': "Quiz 1", 'questions': [{'intitule': "De quelle couleur est le ciel quand il fait beau ?", "propositions": ["Orange", "Bleu", "Rouge", "Violet"], "reponse": ["Bleu"]}, {'intitule': "Façon de dire bonjour", "propositions": ["Bonjour", "Oui", "Baguette", "Heyy"], "reponse": ["Heyy", "Bonjour"]}]},
        {'id': 2, 'name': "Quiz 2", 'questions': [{'intitule': "Test", "propositions": ["Oui", "Test", "Coucou"], "reponse": ["Test"]}, {'intitule': "Hehe", "propositions": ["Oui", "Hehe", "Coucou"], "reponse": ["Hehe"]}, {'intitule': "Inverse de oui", "propositions": ["Oui", "Non", "Peut-être", "Coucou"], "reponse": ["Non"]}]},
        {'id': 3, 'name': "Quiz 3", 'questions': [{'intitule': "Question 1", "propositions": ["Oui", "Baguette", "Coucou"], "reponse": ["Baguette"]}]}
      ]
    };
  },
  components: {
    QuizItem
  }
};
</script>

<style scoped>
</style>

<template>
    <div>
        <ul>
            <li v-for="quiz in quizs" @click="questions(quiz)">{{ quiz.name }}</li>
        </ul>
        <div v-if="selectedQuiz">
            <h2>{{ selectedQuiz.name }}</h2>
            <ol>
                <li v-for="question in selectedQuizQuestions" :key="question.intitule">
                    {{ question.intitule }}
                </li>
            </ol>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        quizs: Array
    },
    data() {
        return {
            selectedQuiz: null
        };
    },
    methods: {
        questions(quiz) {
            this.selectedQuiz = quiz;
        }
    },
    computed: {
        selectedQuizQuestions() {
            // Check if selectedQuiz is null before accessing its properties
            if (this.selectedQuiz) {
                return this.selectedQuiz.questions;
            } else {
                return [];
            }
        }
    }
}
</script>

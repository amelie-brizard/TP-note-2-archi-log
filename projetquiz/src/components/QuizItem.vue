<template>
    <div>
        <h2>Ajouter un quiz</h2>
        <label for="name">Nom : </label>
        <input type="text" id="name" v-model="name">
        <button @click="ajoutQuiz(name)">Ajouter quiz</button>
    </div>
    <div>
        <h2>Consulter les quiz</h2>
        <ul>
            <li v-for="quiz in quizs" :key="quiz.id" @click="questions(quiz)">{{ quiz.name }}</li>
        </ul>
        <div v-if="selectedQuiz">
            <button>Supprimer</button>
            <button>Modifier</button>
            <h2>{{ selectedQuiz.name }}</h2>
            <ol>
                <li v-for="question in selectedQuizQuestions" :key="question.intitule">
                    <fieldset>
                        <legend>{{ question.intitule }}</legend>
                        <div v-if="question.reponse.length === 1">
                            <div v-for="(prop, index) in question.propositions" :key="index">
                                <input type="radio" :id="prop + '-' + question.intitule" :name="question.intitule" :value="prop" />
                                <label :for="prop + '-' + question.intitule">{{ prop }}</label>
                            </div>
                        </div>
                        <div v-else>
                            <div v-for="(prop, index) in question.propositions" :key="index">
                                <input type="checkbox" :id="question.intitule + '-checkbox-' + index" :value="prop" />
                                <label :for="question.intitule + '-checkbox-' + index">{{ prop }}</label>
                            </div>
                        </div>
                    </fieldset>
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
        },
        ajoutQuiz(nameQuiz) {
            let newQuiz = {
                id: this.quizs.length + 1,
                name: nameQuiz,
                questions: []
            };
            this.quizs.push(newQuiz);
        }
    },
    computed: {
        selectedQuizQuestions() {
            if (this.selectedQuiz) {
                return this.selectedQuiz.questions;
            } else {
                return [];
            }
        }
    }
}
</script>

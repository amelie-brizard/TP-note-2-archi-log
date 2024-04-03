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
            <button @click="supprimerQuiz(selectedQuiz.id)">Supprimer</button>
            <button @click="toggleModifierQuestions">Modifier</button>
            <h2>{{ selectedQuiz.name }}</h2>
            <ol v-if="!modifierQuestions">
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
            <ol v-else>
                <button @click="ajouterQuestion()">Ajouter une question</button>
                <li v-for="(question, index) in selectedQuizQuestions" :key="index">
                    <fieldset>
                        <legend>{{ question.intitule }}</legend>
                        <button @click="ajoutProposition(index)">Ajouter proposition</button>
                        <div v-if="question.reponse.length === 1">
                            <div v-for="(prop, index) in question.propositions" :key="index">
                                <input type="radio" :id="prop + '-' + question.intitule" :name="question.intitule" :value="prop" />
                                <label :for="prop + '-' + question.intitule">{{ prop }}</label>
                                <button @click="supprimerQuestion(index)">Supprimer</button>
                                <button @click="modifierQuestion(index)">Modifier</button>
                            </div>
                            <p>Réponses : {{ question.reponse }}</p>
                            <button @click="ajouterReponse(index)">Ajouter une réponse</button>
                        </div>
                        <div v-else>
                            <div v-for="(prop, index) in question.propositions" :key="index">
                                <input type="checkbox" :id="question.intitule + '-checkbox-' + index" :value="prop" />
                                <label :for="question.intitule + '-checkbox-' + index">{{ prop }}</label>
                                <button @click="supprimerQuestion(index)">Supprimer</button>
                                <button @click="modifierQuestion(index)">Modifier</button>
                            </div>
                            <p>Réponses : {{ question.reponse }}</p>
                            <button @click="ajouterReponse(index)">Ajouter une réponse</button>
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
            selectedQuiz: null,
            modifierQuestions: false
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
        },
        supprimerQuiz(idQuiz) {
            this.$emit('removeQuiz', idQuiz);
            location.reload();
        },
        toggleModifierQuestions() {
            this.modifierQuestions = !this.modifierQuestions;
        },
        ajouterQuestion() {
            let intituleQuestion = prompt("Intitulé de la question : ");
            let newQuestion = {
                intitule: intituleQuestion,
                propositions: [],
                reponse: []
            }
            this.selectedQuiz.questions.push(newQuestion);
        },
        modifierQuestion(index) {
            let newTitle = prompt("Modifier l'intitulé de la question :");
            this.selectedQuiz.questions.propositions[index] = newTitle;
            this.$emit('modifierQuestion', index);
        },
        supprimerQuestion(index) {
            console.log(this.selectedQuiz.questions);
            this.$emit('supprimerQuestion', this.selectedQuiz.questions[index]);
            location.reload();
        },
        ajoutProposition(indexQ) {
            let proposition = prompt("Ecrivez une proposition de réponse : ");
            this.selectedQuiz.questions[indexQ].propositions.push(proposition);
        },
        ajouterReponse(index) {
            let reponse = prompt("Ecrivez une réponse : ");
            this.selectedQuiz.questions[index].reponse.push(reponse);
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
    },
    emits: ['removeQuiz', 'supprimerQuestion', 'modifierQuestion']
}
</script>

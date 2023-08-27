<script setup>
import loanRequestService from "@/services/loanRequestService";
import questionService from "@/services/questionService";
import { onMounted, ref } from "vue";

const questions = ref([]);
const form = ref({}); // A form component should be used instead of a simple object

onMounted(() => {
  getQuestions();
});

const getQuestions = async () => {
  const response = await questionService.index({ active: true }); // Pagination is not implemented yet (should be a for)
  questions.value = await response.data;
};

function validate() {
  const errors = [];
  questions.value.map((item) => {
    if ([undefined, "", null].includes(form.value[item.key]) && item.required) {
      errors.push(`O campo "${item.label}" é obrigatório!`);
    }
  });
  return errors;
}

function formatForm() {
  const formattedForm = new FormData();
  Object.keys(form.value).map((item, index) => {
    const value =
      typeof form.value[item] === "object"
        ? form.value[item].name
        : form.value[item];
    formattedForm.append(
      `response.${index}.question_label`,
      questions.value.find((question) => question.key === item).label
    );
    formattedForm.append(
      `response.${index}.question_key`,
      questions.value.find((question) => question.key === item).key
    );
    formattedForm.append(`response.${index}.value`, value);
    if (typeof form.value[item] === "object") {
      formattedForm.append(`response.${index}.file`, form.value[item]);
    }
  });
  return formattedForm;
}

async function submit() {
  const errors = validate();
  if (errors.length > 0) {
    alert(errors.join("\n"));
    return;
  }
  const form = formatForm();
  try {
    loanRequestService.create(form, { "Content-Type": "multipart/form-data" });
    alert("Requisição enviada com sucesso!");
  } catch (error) {
    alert("Ocorreu um erro ao enviar a requisição!");
  } // An toast component should be used instead of alert
}
</script>
<template>
  <main class="bg-purple-900 min-h-screen py-8">
    <section class="mx-auto rounded bg-white p-4 w-full max-w-xl">
      <h1 class="font-black text-4xl">Requisição de empréstimo:</h1>
      <form>
        <template v-for="question in questions">
          <div class="flex flex-col my-4">
            <label :for="question.key" class="text-lg">
              {{ question.label }}
            </label>
            <input
              v-if="question.type === 'text' || question.type === 'number'"
              :id="question.key"
              v-model="form[question.key]"
              class="border rounded p-2"
            />
            <select
              v-if="question.type === 'select'"
              :id="question.key"
              v-model="form[question.key]"
              class="border rounded p-2"
            >
              <option
                v-for="option in question.questionoption_set"
                :value="option.label"
              >
                {{ option.label }}
              </option>
            </select>
            <input
              v-if="question.type === 'file'"
              type="file"
              :id="question.key"
              @change="form[question.key] = $event.target.files[0]"
              class="border rounded p-2"
            />
          </div>
        </template>
        <button
          type="button"
          class="bg-purple-700 text-white px-4 py-2"
          @click="submit"
        >
          Enviar
        </button>
      </form>
    </section>
  </main>
</template>

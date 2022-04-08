import json


wrong_filenames = "retail_recommendations_ai_docs_faq", "windows_faq"

with open('cloud_faq_dataset_raw.jsonl', 'r') as i_fd:
    with open('cloud_faq_dataset_clean.jsonl', 'w') as o_fd:
        for json_line in i_fd:
            line = json.loads(json_line)
            filename = line['filename']
            if line['filename'] in wrong_filenames:
                continue

            origin_question = line['question']
            answer = line['answer']
            if '?' in answer:
                question_in_answer = answer[:answer.index('?') + 1]

                if question_in_answer not in origin_question:
                    continue

                answer = answer.replace(question_in_answer, '').strip()
                if not answer or '?' in answer:
                    continue

                line['answer'] = answer

            o_fd.write(json.dumps(line) + '\n')







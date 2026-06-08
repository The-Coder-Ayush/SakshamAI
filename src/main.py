from pdf_reader import extract_text
from classifier import classify_document
from topic_extractor import extract_topic

from concept_extractor import (
    extract_concepts,
    extract_difficult_words
)

from auto_flowchart import generate_auto_flowchart

from learning_objectives import (
    generate_learning_objectives
)

from student_level import (
    get_student_level,
    get_language
)

from language_detector import detect_language

from teacher_engine import (
    generate_explanation,
    generate_memory_trick,
    generate_question,
    generate_answer,
    generate_dictionary
)

from translator import translate_text

from diagram_extractor import extract_images
from diagram_classifier import classify_diagram
from diagram_explainer import explain_diagram
from rag_engine import RAGEngine


PDF_PATH = "uploads/sample.pdf"


def main():

    print("\nReading PDF...\n")

    content = extract_text(PDF_PATH)
    
     

    rag = RAGEngine(
    content
    )

    # ==================================================
    # DIAGRAM MODE
    # ==================================================

    if not content.strip():

        print("\nNo text found in PDF.")
        print("Switching to Diagram Mode...\n")

        images = extract_images(PDF_PATH)

        print(f"Images Found: {len(images)}\n")

        if len(images) == 0:
            print("No diagrams found.")
            return

        print("Detected Images:\n")

        student_level = get_student_level()
        language = get_language()

        for image in images:

            print(f"\nImage: {image}")

            try:

                diagram_name = classify_diagram(
                    image
                )

                print(
                    f"\nDetected Diagram: {diagram_name}"
                )

                explanation = explain_diagram(
                    diagram_name,
                    student_level
                )

                if language != "English":

                    explanation = translate_text(
                        explanation,
                        language
                    )

                print("\n" + "=" * 70)
                print(explanation)
                print("=" * 70)

            except Exception as e:

                print(
                    f"Diagram Classification Error: {e}"
                )

        return

    # ==================================================
    # TEXT MODE
    # ==================================================

    topic = extract_topic(content)

    print(f"\nDetected Topic: {topic}")

    student_level = get_student_level()

    language = get_language()

    if language == "Auto":

        language = detect_language(
            content
        )

    print(f"\nLanguage: {language}")

    document_type = classify_document(
        content
    )

    concepts = extract_concepts(
        content
    )
    print("\nCONCEPTS FOUND:")
    print(concepts)

    difficult_words = (
        extract_difficult_words(
            concepts
        )
    )

    learning_objectives = (
        generate_learning_objectives(
            topic
        )
    )

    flowchart = generate_auto_flowchart(
        concepts
    )

    print("\nPDF Loaded Successfully")

    print(
        f"\nDocument Type: {document_type}"
    )

    print(
        f"\nCharacters Found: {len(content)}"
    )

    print(
        f"\nSelected Level: {student_level}"
    )

    print("\nImportant Concepts:\n")

    for concept in concepts:
        print(f"- {concept}")

    print("\nDifficult Words:\n")

    for word in difficult_words:
        print(f"- {word}")

    print("\nLearning Objectives:\n")

    for objective in learning_objectives:
        print(f"- {objective}")

    print("\nGenerating Explanation...\n")

    explanation_data = generate_explanation(
    topic,
    concepts,
    rag,
    student_level,
    language
     )

    explanation = explanation_data["explanation"]

    confidence_score = explanation_data["confidence_score"]

    confidence_level = explanation_data["confidence_level"]

    memory_trick = generate_memory_trick(
        topic,
        concepts,
        rag,
        language
    )

    question = generate_question(
        topic,
        concepts,
        rag,
        student_level,
        language
    
    )

    answer = generate_answer(
        topic,
        concepts,
        rag,
        question,
        language
    )

    dictionary = generate_dictionary(
        difficult_words,
        language
    )

    

    print("\n" + "=" * 70)

    print("\n📘 TOPIC\n")
    print(topic)

    print("\n🌱 EXPLANATION\n")
    print(explanation)
    print("\n📊 RETRIEVAL CONFIDENCE")

    print(
    f"Score: {confidence_score}%"
    )

    print(
    f"Level: {confidence_level}"
    )

    print("\n🔄 AUTO FLOWCHART\n")
    print(flowchart)

    print("\n📖 DIFFICULT WORDS\n")
    print(dictionary)

    print("\n🎯 LEARNING OBJECTIVES\n")

    for objective in learning_objectives:
        print(f"• {objective}")

    print("\n🧠 MEMORY TRICK\n")
    print(memory_trick)

    print("\n🤔 CHECK YOURSELF\n")
    print(question)

    print("\nThink before scrolling...\n")

    print("✅ ANSWER SECTION\n")
    print(answer)

    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
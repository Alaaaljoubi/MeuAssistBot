import pandas as pd
import torch
import os
import shutil
from sklearn.model_selection import train_test_split
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset

# Path to results directory
results_dir = '/Users/anasalsayed/Documents/PROJECTS/MeuAssistBot/backend/results'
model_save_path = '/Users/anasalsayed/Documents/PROJECTS/MeuAssistBot/backend/models/my_model'

def delete_last_checkpoint(results_dir):
    checkpoints = [os.path.join(results_dir, d) for d in os.listdir(results_dir) if d.startswith("checkpoint-")]
    checkpoints.sort(key=os.path.getmtime)
    if len(checkpoints) > 1:
        shutil.rmtree(checkpoints[0])

def find_latest_checkpoint(results_dir):
    checkpoints = [os.path.join(results_dir, d) for d in os.listdir(results_dir) if d.startswith("checkpoint-")]
    if checkpoints:
        checkpoints.sort(key=os.path.getmtime)
        return checkpoints[-1]
    return None

if __name__ == "__main__":
    # Load the dataset
    df = pd.read_csv('./data/labeled_data.csv')

    # Encode labels as integers
    label_to_id = {'performance': 0, 'department': 1, 'employee': 2, 'counseling': 3}
    df['label'] = df['label'].map(label_to_id)

    # Prepare the data
    train_texts, val_texts, train_labels, val_labels = train_test_split(df['question'].tolist(), df['label'].tolist(), test_size=0.2)

    # Initialize the tokenizer
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    # Tokenize the data
    train_encodings = tokenizer(train_texts, truncation=True, padding=True, max_length=512)
    val_encodings = tokenizer(val_texts, truncation=True, padding=True, max_length=512)

    # Convert to datasets
    train_dataset = Dataset.from_dict({
        'input_ids': train_encodings['input_ids'],
        'attention_mask': train_encodings['attention_mask'],
        'labels': train_labels
    })

    val_dataset = Dataset.from_dict({
        'input_ids': val_encodings['input_ids'],
        'attention_mask': val_encodings['attention_mask'],
        'labels': val_labels
    })

    # Load the model
    model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=4)

    latest_checkpoint = find_latest_checkpoint(results_dir)

    # Define training arguments
    training_args = TrainingArguments(
        output_dir=results_dir,
        num_train_epochs=3,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        warmup_steps=500,
        weight_decay=0.01,
        logging_dir='./logs',
        logging_steps=10,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        dataloader_num_workers=4,
        fp16=False,  # Disable mixed precision training
        resume_from_checkpoint=latest_checkpoint  # Resume from the last checkpoint if available
    )

    # Initialize Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset
    )

    # Train the model with callback to delete the last checkpoint
    trainer.train()
    trainer.save_model(model_save_path)
    tokenizer.save_pretrained(model_save_path)
    delete_last_checkpoint(results_dir)

    # Save the final model
    model.save_pretrained(model_save_path)
    tokenizer.save_pretrained(model_save_path)

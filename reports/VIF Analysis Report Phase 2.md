VIF Analysis Report
The Variance Inflation Factor (VIF) analysis was conducted on the fused dataset's numerical features (excluding employee_id). VIF measures multicollinearity, with values >10 indicating high collinearity that can destabilize models. Below is the full sorted VIF table:

FeatureVIFstruct_hours_worked42.58behav_punctuality_score40.85struct_client_satisfaction_score25.81audio_speaking_speed25.40behav_work_engagement_score24.44behav_collaboration_score24.20audio_speech_clarity_score24.15struct_average_task_quality24.08struct_efficiency_score24.05struct_deadline_met_score24.02behav_peer_interaction_score23.85behav_task_followup_score23.84struct_tasks_completed12.24audio_speech_energy_level9.90behav_training_hours_completed9.08behav_meetings_attended8.47audio_tone_consistency_score4.71behav_initiative_score4.68struct_innovation_score4.68audio_volume_stability_score4.65audio_pitch_variation4.62audio_pause_frequency3.39struct_projects_led2.94audio_speech_sentiment_score1.01
High VIF Features (>10):
These 13 features exhibit significant multicollinearity and were candidates for removal:

struct_hours_worked (42.58)
behav_punctuality_score (40.85)
struct_client_satisfaction_score (25.81)
audio_speaking_speed (25.40)
behav_work_engagement_score (24.44)
behav_collaboration_score (24.20)
audio_speech_clarity_score (24.15)
struct_average_task_quality (24.08)
struct_efficiency_score (24.05)
struct_deadline_met_score (24.02)
behav_peer_interaction_score (23.85)
behav_task_followup_score (23.84)
struct_tasks_completed (12.24)

No VIF exceeded 50, but values >10 suggest redundancy, aligning with the correlation matrix findings (|corr| >0.85 pairs like struct_hours_worked ↔ struct_tasks_completed).
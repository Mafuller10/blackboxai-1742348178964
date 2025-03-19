from app import create_app
from models import db
from models.user import User
from models.resources import Subject, Worksheet, LessonPlan, Game, Activity

def init_db():
    """Initialize the database with sample data"""
    app = create_app()
    
    with app.app_context():
        # Create admin user
        if not User.query.filter_by(email='admin@classtle.com').first():
            admin = User(
                username='admin',
                email='admin@classtle.com',
                is_premium=True
            )
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print("Created admin user")
        
        # Create subjects
        subjects_data = [
            {
                'name': 'Mathematics',
                'description': 'Numbers, algebra, geometry, and more',
                'grade_level': 'K-12'
            },
            {
                'name': 'Science',
                'description': 'Physics, chemistry, biology, and earth science',
                'grade_level': 'K-12'
            },
            {
                'name': 'English',
                'description': 'Reading, writing, grammar, and literature',
                'grade_level': 'K-12'
            },
            {
                'name': 'History',
                'description': 'World history, civilizations, and social studies',
                'grade_level': 'K-12'
            }
        ]
        
        for subject_data in subjects_data:
            if not Subject.query.filter_by(name=subject_data['name']).first():
                subject = Subject(**subject_data)
                db.session.add(subject)
        db.session.commit()
        print("Created subjects")
        
        # Get references
        admin = User.query.filter_by(email='admin@classtle.com').first()
        math = Subject.query.filter_by(name='Mathematics').first()
        science = Subject.query.filter_by(name='Science').first()
        english = Subject.query.filter_by(name='English').first()
        
        # Create sample worksheets
        worksheets_data = [
            {
                'title': 'Addition and Subtraction',
                'description': 'Practice basic addition and subtraction problems',
                'grade_level': '1-2',
                'difficulty': 'easy',
                'subject_id': math.id,
                'author_id': admin.id,
                'content': 'Sample worksheet content'
            },
            {
                'title': 'Scientific Method',
                'description': 'Learn the steps of the scientific method',
                'grade_level': '3-5',
                'difficulty': 'medium',
                'subject_id': science.id,
                'author_id': admin.id,
                'content': 'Sample worksheet content'
            }
        ]
        
        for worksheet_data in worksheets_data:
            if not Worksheet.query.filter_by(title=worksheet_data['title']).first():
                worksheet = Worksheet(**worksheet_data)
                db.session.add(worksheet)
        db.session.commit()
        print("Created worksheets")
        
        # Create sample lesson plans
        lesson_plans_data = [
            {
                'title': 'Introduction to Fractions',
                'description': 'Basic concepts of fractions',
                'objectives': 'Understand what fractions are and how to use them',
                'materials': 'Paper, pencil, fraction circles',
                'procedure': 'Step by step guide to teaching fractions',
                'assessment': 'Quiz on fractions',
                'duration': '45 minutes',
                'grade_level': '3-4',
                'subject_id': math.id,
                'author_id': admin.id
            },
            {
                'title': 'Parts of Speech',
                'description': 'Learn about nouns, verbs, and adjectives',
                'objectives': 'Identify different parts of speech',
                'materials': 'Worksheet, pencil',
                'procedure': 'Interactive lesson on parts of speech',
                'assessment': 'Writing exercise',
                'duration': '30 minutes',
                'grade_level': '2-3',
                'subject_id': english.id,
                'author_id': admin.id
            }
        ]
        
        for plan_data in lesson_plans_data:
            if not LessonPlan.query.filter_by(title=plan_data['title']).first():
                plan = LessonPlan(**plan_data)
                db.session.add(plan)
        db.session.commit()
        print("Created lesson plans")
        
        # Create sample games
        games_data = [
            {
                'title': 'Multiplication Race',
                'description': 'Practice multiplication facts in a fun racing game',
                'game_type': 'math',
                'difficulty': 'medium',
                'instructions': 'Solve multiplication problems to move your car forward',
                'grade_level': '3-4',
                'subject_id': math.id
            },
            {
                'title': 'Word Builder',
                'description': 'Build words from given letters',
                'game_type': 'language',
                'difficulty': 'easy',
                'instructions': 'Drag and drop letters to form words',
                'grade_level': '1-2',
                'subject_id': english.id
            }
        ]
        
        for game_data in games_data:
            if not Game.query.filter_by(title=game_data['title']).first():
                game = Game(**game_data)
                db.session.add(game)
        db.session.commit()
        print("Created games")
        
        # Create sample activities
        activities_data = [
            {
                'title': 'Build a Volcano',
                'description': 'Create a model volcano and learn about chemical reactions',
                'activity_type': 'science_experiment',
                'materials_needed': 'Baking soda, vinegar, clay, paint',
                'instructions': 'Step by step guide to building a volcano',
                'duration': '1 hour',
                'grade_level': '4-5'
            },
            {
                'title': 'Write a Story',
                'description': 'Creative writing exercise',
                'activity_type': 'writing_prompt',
                'materials_needed': 'Paper, pencil',
                'instructions': 'Write a story about a magical adventure',
                'duration': '45 minutes',
                'grade_level': '3-4'
            }
        ]
        
        for activity_data in activities_data:
            if not Activity.query.filter_by(title=activity_data['title']).first():
                activity = Activity(**activity_data)
                db.session.add(activity)
        db.session.commit()
        print("Created activities")
        
        print("Database initialized successfully!")

if __name__ == '__main__':
    init_db()
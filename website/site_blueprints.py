from flask import Blueprint, render_template

blueprint = Blueprint('blueprint', __name__, static_folder='static', template_folder='templates')

# Cache will be injected by main.py
cache = None

def init_cache(cache_instance):
    """Initialize cache from main.py"""
    global cache
    cache = cache_instance

@blueprint.route('/')
def home():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='home')
        def _cached():
            return render_template("home.html")
        return _cached()
    return render_template("home.html")

@blueprint.route('/bios')
def bios():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='bios')  # 24 hours
        def _cached():
            return render_template('bios.html')
        return _cached()
    return render_template('bios.html')

@blueprint.route('/problem')
def problem():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='problem')
        def _cached():
            return render_template('problem.html')
        return _cached()
    return render_template('problem.html')

@blueprint.route('/solution')
def solution():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='solution')
        def _cached():
            return render_template('solution.html')
        return _cached()
    return render_template('solution.html')

@blueprint.route('/feasibility-v1')
def feasibility_version_one():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='feasibility_v1')
        def _cached():
            return render_template('feasibility-slides-version-1.html')
        return _cached()
    return render_template('feasibility-slides-version-1.html')

@blueprint.route('/feasibility-v2')
def feasibility_version_two():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='feasibility_v2')
        def _cached():
            return render_template('feasibility-slides-version-2.html')
        return _cached()
    return render_template('feasibility-slides-version-2.html')

@blueprint.route('/feasibility-v3')
def feasibility_version_three():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='feasibility_v3')
        def _cached():
            return render_template('feasibility-slides-version-3.html')
        return _cached()
    return render_template('feasibility-slides-version-3.html')

@blueprint.route('/feasibility-v4')
def feasibility_version_four():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='feasibility_v4')
        def _cached():
            return render_template('feasibility-slides-version-4.html')
        return _cached()
    return render_template('feasibility-slides-version-3.html')

@blueprint.route('/final-feasibility')
def final_feasibility():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='final_feasibility')
        def _cached():
            return render_template('final-feasibility-slides.html')
        return _cached()
    return render_template('final-feasibility-slides.html')

@blueprint.route('/design-final')
def design_final():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='design_final')
        def _cached():
            return render_template('design-slides-final.html')
        return _cached()
    return render_template('design-slides-final.html')

@blueprint.route('/design-v1')
def design_version_one():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='design_version_one')
        def _cached():
            return render_template('design-slides-version-1.html')
        return _cached()
    return render_template('design-slides-version-1.html')

@blueprint.route('/design-v2')
def design_version_two():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='design_version_two')
        def _cached():
            return render_template('design-slides-version-2.html')
        return _cached()
    return render_template('design-slides-version-2.html')

@blueprint.route('/design-v3')
def design_version_three():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='design_version_three')
        def _cached():
            return render_template('design-slides-version-3.html')
        return _cached()
    return render_template('design-slides-version-3.html')

@blueprint.route('/design-v4')
def design_version_four():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='design_version_four')
        def _cached():
            return render_template('design-slides-version-4.html')
        return _cached()
    return render_template('design-slides-version-4.html')

@blueprint.route('/prototype-v0')
def prototype_presentation_v0():
    if cache:
        @cache.cached(timeout=3_600, key_prefix='prototype_presentation_v0')
        def _cached():
            return render_template('prototype-slides-version-0.html')
        return _cached()
    return render_template('prototype-slides-version-0.html')

@blueprint.route('/prototype-v1')
def prototype_presentation_v1():
    if cache:
        @cache.cached(timeout=3_600, key_prefix='prototype_presentation_v0')
        def _cached():
            return render_template('prototype-slides-version-0.html')
        return _cached()
    return render_template('prototype-slides-version-0.html')

@blueprint.route('/prototype-v2')
def prototype_presentation_v2():
    if cache:
        @cache.cached(timeout=3_600, key_prefix='prototype_presentation_v0')
        def _cached():
            return render_template('prototype-slides-version-0.html')
        return _cached()
    return render_template('prototype-slides-version-0.html')

@blueprint.route('/prototype-v3')
def prototype_presentation_v3(): # Change to v3 on next iteration
    if cache:
        @cache.cached(timeout=3_600, key_prefix='prototype_presentation_v3')
        def _cached():
            return render_template('prototype-slides-version-3.html')
        return _cached()
    return render_template('prototype-slides-version-3.html')

@blueprint.route('/labs')
def labs():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='labs')
        def _cached():
            return render_template('labs.html')
        return _cached()
    return render_template('labs.html')

@blueprint.route('/lab-1')
def lab_one():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='lab_one')
        def _cached():
            return render_template('lab1.html')
        return _cached()
    return render_template('lab1.html')

@blueprint.route('/lab-2')
def lab_two():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='lab_two')
        def _cached():
            return render_template('lab2.html')
        return _cached()
    return render_template('lab2.html')

@blueprint.route('/deliverables')
def deliverables():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='deliverables')
        def _cached():
            return render_template('deliverables.html')
        return _cached()
    return render_template('deliverables.html')

@blueprint.route('/stories')
def stories():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='stories')
        def _cached():
            return render_template('stories.html')
        return _cached()
    return render_template('stories.html')

@blueprint.route('/references')
def references():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='references')
        def _cached():
            return render_template('references.html')
        return _cached()
    return render_template('references.html')

@blueprint.route('/glossary')
def glossary():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='glossary')
        def _cached():
            return render_template('glossary.html')
        return _cached()
    return render_template('glossary.html')

@blueprint.route('/easter-egg')
def easter_egg():
    if cache:
        @cache.cached(timeout=86_400, key_prefix='easter_egg')
        def _cached():
            return render_template('ee.html')
        return _cached()
    return render_template('ee.html')

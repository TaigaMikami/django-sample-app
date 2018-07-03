from django.views import generic
from .forms import SearchForm
from .models import Employee

class IndexView(generic.ListView):
  template_name = 'employ/employ_list.html'
  model = Employee
  paginate_by = 2

  def get_context_data(self):
    # テンプレートへ渡す辞書の作成
    context = super().get_context_data()
    context['form'] = SearchForm(self.request.GET)
    return context
  
  def get_queryset(self):
    # テンプレートへ渡す[employee_list]を作成する
    form = SearchForm(self.request.GET)
    form.is_valid()
    
    # 全社員を取得
    queryset = super().get_queryset()

    # 部署の洗濯があれあb、部署で絞り込み(filter)
    department = form.cleaned_data['department']
    if department:
      queryset = queryset.filter(department=department)

    # サークルで選択があれば、サークルで絞り込み
    club = form.cleaned_data['club']
    if club:
      queryset = queryset.filter(club=club)

    return queryset
  


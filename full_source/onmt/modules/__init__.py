from __future__ import absolute_import
from onmt.modules.UtilClass import LayerNorm, Elementwise, PositionwiseFeedForward, FeedForward
from onmt.modules.Gate import context_gate_factory, ContextGate
from onmt.modules.GlobalAttention import GlobalAttention
from onmt.modules.Attention import Attention
from onmt.modules.ConvMultiStepAttention import ConvMultiStepAttention
from onmt.modules.ImageEncoder import ImageEncoder
from onmt.modules.AudioEncoder import AudioEncoder
from onmt.modules.CopyGenerator import CopyGenerator, CopyGeneratorLossCompute
from onmt.modules.StructuredAttention import MatrixTree
from onmt.modules.Transformer import \
   TransformerEncoder, TransformerDecoder
from onmt.modules.Conv2Conv import CNNEncoder, CNNDecoder
from onmt.modules.MultiHeadedAttn import MultiHeadedAttention
from onmt.modules.StackedRNN import StackedLSTM, StackedGRU
from onmt.modules.Embeddings import Embeddings, PositionalEncoding
from onmt.modules.WeightNorm import WeightNormConv2d
from onmt.modules.HierarchicalContext import HierarchicalContext

from onmt.Models import EncoderBase, MeanEncoder, StdRNNDecoder, \
    RNNDecoderBase, InputFeedRNNDecoder, RNNEncoder, NMTModel

from onmt.modules.SRU import check_sru_requirement
can_use_sru = check_sru_requirement()
if can_use_sru:
    from onmt.modules.SRU import SRU


# For flake8 compatibility.
__all__ = [EncoderBase, MeanEncoder, RNNDecoderBase, InputFeedRNNDecoder,
           RNNEncoder, NMTModel,
           StdRNNDecoder, ContextGate, GlobalAttention, ImageEncoder,
           PositionwiseFeedForward, PositionalEncoding,
           CopyGenerator, MultiHeadedAttention, Attention,
           LayerNorm, PositionwiseFeedForward, FeedForward,
           TransformerEncoder, TransformerDecoder, Embeddings, Elementwise,
           MatrixTree, WeightNormConv2d, ConvMultiStepAttention,
           CNNEncoder, CNNDecoder, StackedLSTM, StackedGRU,
           context_gate_factory, CopyGeneratorLossCompute, AudioEncoder, 
       HierarchicalContext]

if can_use_sru:
    __all__.extend([SRU, check_sru_requirement])
